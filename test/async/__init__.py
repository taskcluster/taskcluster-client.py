""" Basic and helper things for testing the Taskcluster Python client"""
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import aiohttp
import aiohttp.client
import aiohttp.client_reqrep
import asyncio
import json
import logging
import mock
import os
import pprint

import taskcluster.exceptions as exceptions
import taskcluster.utils as utils
import test.base as base
from taskcluster.async import Auth


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.NullHandler())
if os.environ.get('DEBUG_TASKCLUSTER_CLIENT'):
    log.addHandler(logging.StreamHandler())


def createFakeApi(cls, *args, **kwargs):
    """For the single async tests, override class.makeHttpRequest().

    Not using MagicMock() directly because it's not an async function.
    """
    instance = cls(*args, **kwargs)
    instance.httpMock = mock.MagicMock()

    async def makeHttpRequest(*args, **kwargs):
        return instance.httpMock(*args, **kwargs)

    instance.makeHttpRequest = makeHttpRequest
    return instance


def createFakeMultiApi(cls, *args, **kwargs):
    """For the mocked multi async tests, save the args+kwargs sent to
    _makeHttpRequest and fail the first _makeHttpRequest attempt.
    """
    instance = cls(*args, **kwargs)
    instance.http_request_count = 0
    instance.http_request_args = []

    async def makeHttpRequest(*args, **kwargs):
        return instance.httpMock(*args, **kwargs)

    async def _makeHttpRequest(*args, **kwargs):
        """Fail the first time!
        """
        instance.http_request_count += 1
        instance.http_request_args.append([args, kwargs])
        if instance.http_request_count < 2:
            raise exceptions.TaskclusterConnectionError("test", None)
        return None

    instance._makeHttpRequest = _makeHttpRequest
    return instance


def getFailFirstSession(firstSuccess=2):
    """For the integration multi async tests, save the clientScopes and
    fail the first attempt.  Similar to createFakeMultiApi, but mock deeper
    in aiohttp instead of AsyncClient._makeHttpRequest.
    """
    session = aiohttp.ClientSession()
    session.count = 0
    session.arg_tracker = []
    async def _fake_request(method, url, *args, **kwargs):
        """Fail the first time!
        """
        session.count += 1
        status = 200
        if session.count < firstSuccess:
            status = 500  # retry
        response = FakeResponse(method, url, status=status)
        data = json.loads(kwargs['data'])
        session.arg_tracker.append(data['clientScopes'][0])
        return response

    session._request = _fake_request
    return session


def getFakeSession(status=200, payload=None, response=None):
    """Return an aiohttp ClientSession with its _request method overridden
    with _fake_request.
    """
    payload = payload or {}

    @asyncio.coroutine
    def _fake_request(method, url, *args, **kwargs):
        if response is not None:
            return response
        return FakeResponse(method, url, status=status, payload=payload)

    session = aiohttp.ClientSession()
    session._request = _fake_request
    return session


def getExceptionSession(exception=aiohttp.ClientError):
    """An aiohttp ClientSession that throws `exception` on _request() and keeps
    count of retries.
    """
    session = aiohttp.ClientSession()
    session.count = 0

    @asyncio.coroutine
    def _fake_request(*args, **kwargs):
        session.count += 1
        raise exception("Fake Exception")

    session._request = _fake_request
    return session


class AsyncGeneratedTC(base.GeneratedTC):
    """Test a generated async class.

    Set self.testClass to the FakeGenerated object
    """
    maxDiff = None
    testClass = None

    def try_function(self, functionName, method, argumentNames=None, validOptions=None):
        """For entry functions, verify the makeHttpRequest arguments are
        correct.
        """
        a = createFakeApi(self.testClass)
        argumentNames = argumentNames or []
        kwargs = {}
        replDict = self._get_replDict(argumentNames)
        expectedRoute = a.routes[functionName].format(**replDict).lstrip('/')

        async def main():
            return await asyncio.wait([
                getattr(a, functionName)(*argumentNames, **kwargs)
            ])

        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        if validOptions:
            kwargs['validOptions'] = validOptions
            kwargs['options'] = None
        expectedArgs = [method, expectedRoute]
        if 'payload' in argumentNames:
            expectedArgs.append('payload')
        a.httpMock.assert_called_once_with(*expectedArgs, **kwargs)

    def try_async_function(self, functionName, method, argumentNames=None, validOptions=None):
        """Test async: a second call should be able to run before a failed
        first call is retried
        """

        a = createFakeMultiApi(self.testClass)

        # Create 2 sets of args so we can tell the two calls apart
        args1 = argumentNames or []
        args2 = ["{}2".format(x) for x in args1]
        kwargs = {}
        replDict1 = self._get_replDict(args1)
        replDict2 = self._get_replDict(args1, suffix="2")
        expectedRoute1 = a.routes[functionName].format(**replDict1).lstrip('/')
        expectedRoute2 = a.routes[functionName].format(**replDict2).lstrip('/')

        async def main():
            return await asyncio.wait([
                getattr(a, functionName)(*args2, **kwargs),
                getattr(a, functionName)(*args1, **kwargs),
            ])

        with mock.patch.object(utils, 'calculateSleepTime') as p:
            p.return_value = .001
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

        args = a.http_request_args
        pprint.pprint(args)
        # The first and third attempts should be the same route;
        # the second attempt should be the unblocked (async) second route
        self.assertTrue(
            (
                args[0][0][1].endswith(expectedRoute1) and
                args[2][0][1].endswith(expectedRoute1) and
                args[1][0][1].endswith(expectedRoute2)
            ) or (
                args[0][0][1].endswith(expectedRoute2) and
                args[2][0][1].endswith(expectedRoute2) and
                args[1][0][1].endswith(expectedRoute1)
            )
        )


class FakeResponse(aiohttp.client_reqrep.ClientResponse):
    """Integration tests allow us to test everything's hooked up to aiohttp
    correctly.  When we don't want to actually hit an external url, have
    the aiohttp session's _request method return a FakeResponse.
    """
    def __init__(self, *args, status=200, payload=None, **kwargs):
        super(FakeResponse, self).__init__(*args, **kwargs)
        self._connection = mock.MagicMock()
        self._payload = payload or {}
        self.status = status
        self.headers = {'content-type': 'application/json'}
        self._loop = mock.MagicMock()

    @asyncio.coroutine
    def text(self, *args, **kwargs):
        return json.dumps(self._payload)

    @asyncio.coroutine
    def json(self, *args, **kwargs):
        return self._payload

    @asyncio.coroutine
    def release(self):
        return


class AsyncAuthentication(base.BaseAuthentication):
    """Async Authentication test class, for integration testing.

    This will be run against the buildtime-generated async Auth class.

    The methods don't begin with test_ because nosetests sniff those out.
    """
    maxDiff = None

    def _get_json(self, url):
        async def _helper_json():
            r = await aiohttp.request('get', url)
            return await r.json()
        return asyncio.get_event_loop().run_until_complete(_helper_json())

    def _get_error(self, url, expectedStatus, **kwargs):
        async def _helper_error():
            return await aiohttp.request('get', url)
        resp = asyncio.get_event_loop().run_until_complete(_helper_error())
        self.assertEqual(expectedStatus, resp.status)

    def _get_result(self, function, *args, **kwargs):
        async def _helper_result():
            return await function(*args, **kwargs)

        result = asyncio.get_event_loop().run_until_complete(_helper_result())
        return result

    def no_creds_needed(self):
        """we can call methods which require no scopes with an unauthenticated
        client"""

        @asyncio.coroutine
        def _fake_request(method, url, *args, **kwargs):
            self.assertEqual(url,
                             'https://auth.taskcluster.net/v1/clients/abc')
            self.failIf('Authorization' in kwargs['headers'])
            return FakeResponse(method, url, payload={"clientId": "abc"})

        session = aiohttp.ClientSession()
        session._request = _fake_request

        client = Auth({"credentials": {}}, session=session)

        async def _helper_client():
            return await client.client('abc')

        result = asyncio.get_event_loop().run_until_complete(_helper_client())
        self.assertEqual(result, {"clientId": "abc"})

    def async_auth(self):
        """Using the permacred_simple test, but with 2 calls.  The first auth call
        will fail, and the 2nd auth call should happen before the first retries.
        """
        session = getFailFirstSession()
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'no-secret',
            }
        }, session=session)
        with mock.patch.object(utils, 'calculateSleepTime') as p:
            p.return_value = .001

            async def main():
                return await asyncio.wait([
                    client.testAuthenticate({
                        'clientScopes': ['test:a'],
                        'requiredScopes': ['test:a'],
                    }),
                    client.testAuthenticate({
                        'clientScopes': ['test:b'],
                        'requiredScopes': ['test:b'],
                    }),
                ])

            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

        pprint.pprint(session.arg_tracker)
        # The first and third attempts should be the same scope;
        # the second attempt should be the unblocked (async) second scope
        self.assertTrue(session.arg_tracker in (['test:a', 'test:b', 'test:a'],
                                                ['test:b', 'test:a', 'test:b']))
