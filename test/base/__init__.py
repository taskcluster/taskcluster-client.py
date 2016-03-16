""" Basic and helper things for testing the Taskcluster Python client"""
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import unittest
import os
import logging
import time
import json
import mock
import re
from operator import itemgetter
from taskcluster.runtimeclient import ROUTING_KEY_BLACKLIST

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
    instance._makeHttpRequest = mock.MagicMock()
    instance._makeTopicExchange = mock.MagicMock()
    return instance


class GeneratedTC(TCTest):
    """Base class to test a generated class.

    Set self.testClass to the FakeGenerated object
    """
    maxDiff = None
    testClass = None

    def _get_replDict(self, argumentNames):
        """Create a replacement dictionary to string format a url.

        Each {var} is replaced with 'var', e.g. {clientId} -> 'clientId'
        """
        a = createFakeApi(self.testClass)
        replDict = {'baseUrl': a.options['baseUrl']}
        for name in argumentNames:
            replDict[name] = name
        return replDict

    def try_function(self, functionName, method, argumentNames=None, validOptions=None):
        """For entry functions, verify the _makeHttpRequest arguments are
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
        a._makeHttpRequest.assert_called_once_with(*expectedArgs, **kwargs)

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
