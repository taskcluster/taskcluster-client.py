from __future__ import division, print_function
import asyncio
import mock
import pprint

from test.async import getExceptionSession, getFailFirstSession, getFakeSession, FakeResponse
from test.base import TCTest
import taskcluster.async.asyncclient as asyncclient
import taskcluster.exceptions as exceptions
import taskcluster.utils as utils


def newClient(*args, **kwargs):
    client = asyncclient.AsyncClient(*args, **kwargs)
    client.options['baseUrl'] = 'https://example.com'
    return client


class TestAsyncclient(TCTest):

    def test_success(self):
        """test_asyncclient | success
        """
        payload = '{"clientScopes": ["a"]}'
        session = getFakeSession(payload=payload)
        client = newClient(session=session)

        result = asyncio.get_event_loop().run_until_complete(
            client.makeHttpRequest('get', 'http://example.com',
                                   '{"clientScopes": ["a"]}', {})
        )
        self.assertEqual(payload, result)

    def test_too_many_retries(self):
        """test_asyncclient | too many retries
        """
        session = getFailFirstSession(firstSuccess=10)
        client = newClient(session=session)

        with mock.patch.object(utils, 'calculateSleepTime') as p:
            p.return_value = .001
            with self.assertRaises(exceptions.TaskclusterRestFailure):
                asyncio.get_event_loop().run_until_complete(
                    client.makeHttpRequest('get', 'http://example.com',
                                           '{"clientScopes": ["a"]}', {})
                )

    def test_exception(self):
        """test_asyncclient | exception retries
        """
        session = getExceptionSession()
        client = newClient(session=session)

        with mock.patch.object(utils, 'calculateSleepTime') as p:
            p.return_value = .001
            with self.assertRaises(exceptions.TaskclusterConnectionError):
                asyncio.get_event_loop().run_until_complete(
                    client._makeHttpRequest('get', 'http://example.com',
                                            '{"clientScopes": ["a"]}',
                                            {}, session=session)
                )

    def test_bad_json_status_200(self):
        """test_asyncclient | bad json 200 status
        """
        response = FakeResponse('get', 'url')

        async def bad_json(*args, **kwargs):
            raise ValueError("blah")

        response.json = bad_json
        session = getFakeSession(response=response)
        client = newClient(session=session)

        result = asyncio.get_event_loop().run_until_complete(
            client._makeHttpRequest('get', 'http://example.com',
                                    '{"clientScopes": ["a"]}',
                                    {}, session=session)
        )
        self.assertEqual(result, {'response': response})

    def test_bad_json_status_404(self):
        """test_asyncclient | bad json non-200 status
        """
        response = FakeResponse('get', 'url', status=404)

        async def bad_json(*args, **kwargs):
            raise ValueError("blah")

        response.json = bad_json
        session = getFakeSession(response=response)
        client = newClient(session=session)

        with self.assertRaises(exceptions.TaskclusterRestFailure):
            asyncio.get_event_loop().run_until_complete(
                client._makeHttpRequest('get', 'http://example.com',
                                        '{"clientScopes": ["a"]}',
                                        {}, session=session)
            )

    def test_auth_error(self):
        """test_asyncclient | AuthenticationError
        """
        response = FakeResponse('get', 'url', status=401)

        async def bad_json(*args, **kwargs):
            raise ValueError("blah")

        response.json = bad_json
        session = getFakeSession(response=response)
        client = newClient(session=session)

        with self.assertRaises(exceptions.TaskclusterAuthFailure):
            asyncio.get_event_loop().run_until_complete(
                client._makeHttpRequest('get', 'http://example.com',
                                        '{"clientScopes": ["a"]}',
                                        {}, session=session)
            )

    def test_status_204(self):
        """test_asyncclient | 204 status
        """
        session = getFakeSession(status=204)
        client = newClient(session=session)

        response = asyncio.get_event_loop().run_until_complete(
            client._makeHttpRequest('get', 'http://example.com',
                                    '{"clientScopes": ["a"]}',
                                    {}, session=session)
        )
        pprint.pprint(response)
        self.assertTrue(response is None)
