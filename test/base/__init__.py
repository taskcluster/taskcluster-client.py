""" Basic and helper things for testing the Taskcluster Python client"""
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import datetime
import httmock
import json
import logging
import mock
import os
import re
import requests
import time
import unittest

from operator import itemgetter
from six.moves import urllib

from taskcluster.runtimeclient import ROUTING_KEY_BLACKLIST
import taskcluster.client as subject
import taskcluster.exceptions as exc


# Mocks really ought not to overwrite this
_sleep = time.sleep

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.NullHandler())
if os.environ.get('DEBUG_TASKCLUSTER_CLIENT'):
    log.addHandler(logging.StreamHandler())

SOURCE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'taskcluster'
)
APIS_JSON_FILE = os.path.join(SOURCE_DIR, 'apis.json')
with open(APIS_JSON_FILE, "r") as fh:
    APIS_JSON = json.load(fh)


class TCTest(unittest.TestCase):
    """ Let's have a common base class for all Taskcluster-client tests."""
    pass


def createApiRef(**kwargs):
    default = {
        'version': '0.0.1',
        'title': 'API Title',
        'description': 'API Description',
        'baseUrl': 'https://fake.taskcluster.net/v1',
        'exchangePrefix': 'test/v1',
        'entries': []
    }
    default.update(kwargs)
    return {'reference': default}


def createApiEntryFunction(name, numArg, hasInput, method='get', **kwargs):
    if 'route' in kwargs:
        route = kwargs['route']
        fullArgs = [x[1:-1] for x in route.split('/') if x.startswith('<')]
    else:
        fullArgs = ['arg%d' % i for i in range(numArg)]
        routeChunks = ['/<%s>' % j for j in fullArgs]
        route = ''.join(routeChunks)
        route = '/%s%s' % (name, route)

    default = {
        'type': 'function',
        'method': method,
        'route': route,
        'name': name,
        'title': 'Test API Endpoint title',
        'description': 'Test API Endpoint Description',
        'output': 'http://localhost/schemas/v1/apiOutput',
        'args': fullArgs,
    }
    if hasInput:
        default['input'] = 'http://localhost/schemas/v1/apiInput'
    default.update(kwargs)
    return default


def createApiEntryTopicExchange(name, exchange, **kwargs):
    default = {
        'type': 'topic-exchange',
        'exchange': exchange,
        'name': name,
        'title': 'Test Topic Exchange',
        'description': 'Test Topic Exchange Description',
    }
    default.update(kwargs)
    return default


def createTopicExchangeKey(name, constant=None, multipleWords=False, maxSize=5,
                           required=False, **kwargs):
    default = {
        'name': name,
        'summary': 'A short description of the key',
        'maxSize': maxSize,
        'required': required,
        'multipleWords': multipleWords
    }
    if constant:
        default['constant'] = constant
    default.update(kwargs)
    return default


class AuthClient(object):
    def __init__(self, clientId, accessToken, expires, scopes):
        self.clientId = clientId
        self.accessToken = accessToken
        self.expires = expires
        self.scopes = scopes

    def forNode(self):
        return {
            'clientId': self.clientId,
            'accessToken': self.accessToken,
            'expires': self.expires,
            'scopes': self.scopes
        }


def createFakeApi(cls, *args, **kwargs):
    """For generated tests.
    """
    instance = cls(*args, **kwargs)
    instance.makeHttpRequest = mock.MagicMock()
    instance._makeTopicExchange = mock.MagicMock()
    return instance


class GeneratedTC(TCTest):
    """Base class to test a generated class.

    Set self.testClass to the FakeGenerated object
    """
    maxDiff = None
    testClass = None

    def _get_replDict(self, argumentNames, suffix=""):
        """Create a replacement dictionary to string format a url.

        Each {var} is replaced with 'var', e.g. {clientId} -> 'clientId'
        """
        a = createFakeApi(self.testClass)
        replDict = {'baseUrl': a.options['baseUrl']}
        for name in argumentNames:
            replDict[name] = "{}{}".format(name, suffix)
        return replDict

    def try_function(self, functionName, method, argumentNames=None, validOptions=None):
        """For entry functions, verify the makeHttpRequest arguments are
        correct.
        """
        a = createFakeApi(self.testClass)
        argumentNames = argumentNames or []
        kwargs = {}
        replDict = self._get_replDict(argumentNames)
        expectedRoute = a.routes[functionName].format(**replDict).lstrip('/')
        getattr(a, functionName)(*argumentNames, **kwargs)
        if validOptions:
            kwargs['validOptions'] = validOptions
            kwargs['options'] = None
        expectedArgs = [method, expectedRoute]
        if 'payload' in argumentNames:
            expectedArgs.append('payload')
        a.makeHttpRequest.assert_called_once_with(*expectedArgs, **kwargs)

    def try_topic(self, functionName, exchangeName):
        """For entry topic exchanges, verify the _makeTopicExchange arguments
        are correct.
        """
        a = createFakeApi(self.testClass)
        exchangeUrl = '%s/%s' % (a.options['exchangePrefix'].rstrip('/'),
                                 exchangeName)
        getattr(a, functionName)("routingKeyPattern")
        a._makeTopicExchange.assert_called_once_with(
            exchangeUrl,
            a.routingKeys[functionName],
            "routingKeyPattern"
        )

    def route_check(self, className):
        """Make sure self.routes reflects the api.
        """
        routes = {}
        for entry in APIS_JSON[className]['reference']['entries']:
            if entry['type'] == 'function':
                routes[entry['name']] = re.sub('<(.*?)>', '{\\1}', (entry['route']))
        a = createFakeApi(self.testClass)
        if routes:
            self.assertEqual(routes, a.routes)
        else:
            self.assertFalse(hasattr(a, 'routes'))

    def routingKeys_check(self, className):
        """Make sure self.routingKeys reflects the api.

        This is a bit more complicated because the list of dicts is unsorted.
        """
        routingKeys = {}
        for entry in APIS_JSON[className]['reference']['entries']:
            if 'routingKey' in entry:
                routingKeys[str(entry['name'])] = []
                for r in entry['routingKey']:
                    rk = {}
                    for item in r:
                        if item not in ROUTING_KEY_BLACKLIST:
                            rk[item] = r[item]
                    routingKeys[entry['name']].append(rk)
        a = createFakeApi(self.testClass)

        # http://stackoverflow.com/a/73050
        def sort_list_of_dicts(list_to_sort):
            return sorted(list_to_sort, key=itemgetter('name'))

        if routingKeys:
            keys = sorted(routingKeys.keys())
            self.assertEqual(keys, sorted(a.routingKeys.keys()))
            for key in sorted(routingKeys.keys()):
                self.assertEqual(
                    sort_list_of_dicts(routingKeys[key]),
                    sort_list_of_dicts(a.routingKeys[key])
                )
        else:
            self.assertFalse(hasattr(a, 'routingKeys'))


class BaseAuthentication(TCTest):
    """Base Authentication test class, for integration testing.

    This will be run against both the runtime- and buildtime- generated
    Auth classes.

    The methods don't begin with test_ because nosetests sniff those out.
    """

    def testClass(self, *args, **kwargs):
        """Define this with Auth
        """
        pass

    def _get_json(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def _get_error(self, url, expectedStatus,
                   exception=requests.exceptions.RequestException):
        response = requests.get(url)
        with self.assertRaises(exception):
            response.raise_for_status()
        self.assertEqual(expectedStatus, response.status_code)

    def _get_result(self, function, *args, **kwargs):
        return function(*args, **kwargs)

    def no_creds_needed(self):
        """we can call methods which require no scopes with an unauthenticated
        client.

        httmock is requests-specific, so we'll need to override this method for
        async tests.
        """
        # mock this request so we don't depend on the existence of a client
        # TODO make this async override friendly
        @httmock.all_requests
        def auth_response(url, request):
            self.assertEqual(urllib.parse.urlunsplit(url),
                             'https://auth.taskcluster.net/v1/clients/abc')
            self.failIf('Authorization' in request.headers)
            headers = {'content-type': 'application/json'}
            content = {"clientId": "abc"}
            return httmock.response(200, content, headers, None, 5, request)

        with httmock.HTTMock(auth_response):
            client = self.testClass({"credentials": {}})
            result = client.client('abc')
            self.assertEqual(result, {"clientId": "abc"})

    def permacred_simple(self):
        """we can call methods which require authentication with valid
        permacreds"""
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'no-secret',
            }
        })
        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:a'],
            'requiredScopes': ['test:a'],
        })
        self.assertEqual(result, {'scopes': ['test:a'], 'clientId': 'tester'})

    def permacred_simple_authorizedScopes(self):
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'no-secret',
            },
            'authorizedScopes': ['test:a', 'test:b'],
        })
        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:*'],
            'requiredScopes': ['test:a'],
        })
        self.assertEqual(result, {'scopes': ['test:a', 'test:b'],
                                  'clientId': 'tester'})

    def unicode_permacred_simple(self):
        """Unicode strings that encode to ASCII in credentials do not cause issues"""
        client = self.testClass({
            'credentials': {
                'clientId': u'tester',
                'accessToken': u'no-secret',
            }
        })
        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:a'],
            'requiredScopes': ['test:a'],
        })
        self.assertEqual(result, {'scopes': ['test:a'], 'clientId': 'tester'})

    def invalid_unicode_permacred_simple(self):
        """Unicode strings that do not encode to ASCII in credentials cause issues"""
        with self.assertRaises(exc.TaskclusterAuthFailure):
            self._get_result(self.testClass, {
                'credentials': {
                    'clientId': u"\U0001F4A9",
                    'accessToken': u"\U0001F4A9",
                }
            })

    def permacred_insufficient_scopes(self):
        """A call with insufficient scopes results in an error"""
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'no-secret',
            }
        })
        # TODO: this should be TaskclsuterAuthFailure; most likely the client
        # is expecting AuthorizationFailure instead of AuthenticationFailure
        with self.assertRaises(exc.TaskclusterRestFailure):
            self._get_result(client.testAuthenticate, {
                'clientScopes': ['test:*'],
                'requiredScopes': ['something-more'],
            })

    def temporary_credentials(self):
        """we can call methods which require authentication with temporary
        credentials generated by python client"""
        tempCred = subject.createTemporaryCredentials(
            'tester',
            'no-secret',
            datetime.datetime.utcnow() - datetime.timedelta(hours=10),
            datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            ['test:xyz'],
        )
        client = self.testClass({
            'credentials': tempCred,
        })

        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:*'],
            'requiredScopes': ['test:xyz'],
        })
        self.assertEqual(result, {'scopes': ['test:xyz'], 'clientId': 'tester'})

    def named_temporary_credentials(self):
        tempCred = subject.createTemporaryCredentials(
            'tester',
            'no-secret',
            datetime.datetime.utcnow() - datetime.timedelta(hours=10),
            datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            ['test:xyz'],
            name='credName'
        )
        client = self.testClass({
            'credentials': tempCred,
        })

        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:*', 'auth:create-client:credName'],
            'requiredScopes': ['test:xyz'],
        })
        self.assertEqual(result, {'scopes': ['test:xyz'], 'clientId': 'credName'})

    def temporary_credentials_authorizedScopes(self):
        tempCred = subject.createTemporaryCredentials(
            'tester',
            'no-secret',
            datetime.datetime.utcnow() - datetime.timedelta(hours=10),
            datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            ['test:xyz:*'],
        )
        client = self.testClass({
            'credentials': tempCred,
            'authorizedScopes': ['test:xyz:abc'],
        })

        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:*'],
            'requiredScopes': ['test:xyz:abc'],
        })
        self.assertEqual(result, {'scopes': ['test:xyz:abc'],
                                  'clientId': 'tester'})

    def named_temporary_credentials_authorizedScopes(self):
        tempCred = subject.createTemporaryCredentials(
            'tester',
            'no-secret',
            datetime.datetime.utcnow() - datetime.timedelta(hours=10),
            datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            ['test:xyz:*'],
            name='credName'
        )
        client = self.testClass({
            'credentials': tempCred,
            'authorizedScopes': ['test:xyz:abc'],
        })

        result = self._get_result(client.testAuthenticate, {
            'clientScopes': ['test:*', 'auth:create-client:credName'],
            'requiredScopes': ['test:xyz:abc'],
        })
        self.assertEqual(result, {'scopes': ['test:xyz:abc'],
                                  'clientId': 'credName'})

    def signed_url(self):
        """we can use a signed url built with the python client"""
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'no-secret',
            }
        })
        signedUrl = client.buildSignedUrl(methodName='testAuthenticateGet')
        response = self._get_json(signedUrl)
        response['scopes'].sort()
        self.assertEqual(response, {
            'scopes': sorted(['test:*', u'auth:create-client:test:*']),
            'clientId': 'tester',
        })

    def signed_url_bad_credentials(self):
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'wrong-secret',
            }
        })
        signedUrl = client.buildSignedUrl(methodName='testAuthenticateGet')
        self._get_error(signedUrl, 401)

    def temp_credentials_signed_url(self):
        tempCred = subject.createTemporaryCredentials(
            'tester',
            'no-secret',
            datetime.datetime.utcnow() - datetime.timedelta(hours=10),
            datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            ['test:*'],
        )
        client = self.testClass({
            'credentials': tempCred,
        })
        signedUrl = client.buildSignedUrl(methodName='testAuthenticateGet')
        response = self._get_json(signedUrl)
        self.assertEqual(response, {
            'scopes': ['test:*'],
            'clientId': 'tester',
        })

    def signed_url_authorizedScopes(self):
        client = self.testClass({
            'credentials': {
                'clientId': 'tester',
                'accessToken': 'no-secret',
            },
            'authorizedScopes': ['test:authenticate-get'],
        })
        signedUrl = client.buildSignedUrl(methodName='testAuthenticateGet')
        response = self._get_json(signedUrl)
        self.assertEqual(response, {
            'scopes': ['test:authenticate-get'],
            'clientId': 'tester',
        })

    def temp_credentials_signed_url_authorizedScopes(self):
        tempCred = subject.createTemporaryCredentials(
            'tester',
            'no-secret',
            datetime.datetime.utcnow() - datetime.timedelta(hours=10),
            datetime.datetime.utcnow() + datetime.timedelta(hours=10),
            ['test:*'],
        )
        client = self.testClass({
            'credentials': tempCred,
            'authorizedScopes': ['test:authenticate-get'],
        })
        signedUrl = client.buildSignedUrl(methodName='testAuthenticateGet')
        response = self._get_json(signedUrl)
        self.assertEqual(response, {
            'scopes': ['test:authenticate-get'],
            'clientId': 'tester',
        })
