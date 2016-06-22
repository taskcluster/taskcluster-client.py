"""This module is used to interact with taskcluster rest apis"""

from __future__ import absolute_import, division, print_function

import logging
import copy
import six

from taskcluster.baseclient import config
from taskcluster.sync.syncclient import SyncClient
import taskcluster.exceptions as exceptions
import taskcluster.utils as utils

log = logging.getLogger(__name__)

_defaultConfig = copy.deepcopy(config)


class RuntimeClient(SyncClient):

    def _makeApiCall(self, entry, *args, **kwargs):
        """ This function is used to dispatch calls to other functions
        for a given API Reference entry"""

        payload = None
        _args = list(args)
        _kwargs = copy.deepcopy(kwargs)

        if 'input' in entry:
            if len(args) > 0:
                payload = _args.pop()
            else:
                raise exceptions.TaskclusterFailure('Payload is required as last positional arg')
        apiArgs = self._processArgs(entry, *_args, **_kwargs)
        route = self._subArgsInRoute(entry, apiArgs)
        log.debug('Route is: %s', route)

        return self.makeHttpRequest(entry['method'], route, payload)

    def _processArgs(self, entry, *args, **kwargs):
        """ Take the list of required arguments, positional arguments
        and keyword arguments and return a dictionary which maps the
        value of the given arguments to the required parameters.

        Keyword arguments will overwrite positional arguments.
        """

        reqArgs = entry['args']
        data = {}

        # These all need to be rendered down to a string, let's just check that
        # they are up front and fail fast
        for arg in list(args) + [kwargs[x] for x in kwargs]:
            if not isinstance(arg, six.string_types) and not isinstance(arg, int):
                raise exceptions.TaskclusterFailure(
                    'Arguments "%s" to %s is not a string or int' % (arg, entry['name']))

        if len(args) > 0 and len(kwargs) > 0:
            raise exceptions.TaskclusterFailure('Specify either positional or key word arguments')

        # We know for sure that if we don't give enough arguments that the call
        # should fail.  We don't yet know if we should fail because of two many
        # arguments because we might be overwriting positional ones with kw ones
        if len(reqArgs) > len(args) + len(kwargs):
            raise exceptions.TaskclusterFailure(
                '%s takes %d args, only %d were given' % (
                    entry['name'], len(reqArgs), len(args) + len(kwargs)))

        # We also need to error out when we have more positional args than required
        # because we'll need to go through the lists of provided and required args
        # at the same time.  Not disqualifying early means we'll get IndexErrors if
        # there are more positional arguments than required
        if len(args) > len(reqArgs):
            raise exceptions.TaskclusterFailure('%s called with too many positional args',
                                                entry['name'])

        i = 0
        for arg in args:
            log.debug('Found a positional argument: %s', arg)
            data[reqArgs[i]] = arg
            i += 1

        log.debug('After processing positional arguments, we have: %s', data)

        data.update(kwargs)

        log.debug('After keyword arguments, we have: %s', data)

        if len(reqArgs) != len(data):
            errMsg = '%s takes %s args, %s given' % (
                entry['name'],
                ','.join(reqArgs),
                data.keys())
            log.error(errMsg)
            raise exceptions.TaskclusterFailure(errMsg)

        for reqArg in reqArgs:
            if reqArg not in data:
                errMsg = '%s requires a "%s" argument which was not provided' % (
                    entry['name'], reqArg)
                log.error(errMsg)
                raise exceptions.TaskclusterFailure(errMsg)

        return data

    def _makeTopicExchange(self, entry, *args, **kwargs):
        if len(args) == 0 and not kwargs:
            routingKeyPattern = {}
        elif len(args) >= 1:
            if kwargs or len(args) != 1:
                errStr = 'Pass either a string, single dictionary or only kwargs'
                raise exceptions.TaskclusterTopicExchangeFailure(errStr)
            routingKeyPattern = args[0]
        else:
            routingKeyPattern = kwargs

        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 entry['exchange'].lstrip('/'))
        return super(RuntimeClient, self)._makeTopicExchange(
            exchangeUrl, entry['routingKey'], routingKeyPattern
        )

    def buildUrl(self, methodName, *args, **kwargs):
        entry = None
        for x in self._api['entries']:
            if x['name'] == methodName:
                entry = x
        if not entry:
            raise exceptions.TaskclusterFailure(
                'Requested method "%s" not found in API Reference' % methodName)
        apiArgs = self._processArgs(entry, *args, **kwargs)
        route = self._subArgsInRoute(entry, apiArgs)
        return self.makeFullUrl(route)

    def buildSignedUrl(self, methodName, *args, **kwargs):
        expiration = kwargs.get('expiration')
        if 'expiration' in kwargs:
            del kwargs['expiration']
        return super(RuntimeClient, self).buildSignedUrl(
            requestUrl=self.buildUrl(methodName, *args, **kwargs),
            expiration=expiration
        )

    def _subArgsInRoute(self, entry, replDict):
        """ Here for backwards compatibility only.

        Use self.makeRoute.
        """
        return self.makeRoute(entry['name'], entry['route'], replDict)


def createApiClient(name, api):
    attributes = dict(
        name=name,
        _api=api['reference'],
        __doc__=api.get('description'),
        classOptions={},
    )

    copiedOptions = ('baseUrl', 'exchangePrefix')
    for opt in copiedOptions:
        if opt in api['reference']:
            attributes['classOptions'][opt] = api['reference'][opt]

    for entry in api['reference']['entries']:
        if entry['type'] == 'function':

            def addApiCall(e):
                def apiCall(self, *args, **kwargs):
                    return self._makeApiCall(e, *args, **kwargs)
                return apiCall

            f = addApiCall(entry)
            docStr = "Call the %s api's %s method.  " % (name, entry['name'])

            if entry['args'] and len(entry['args']) > 0:
                docStr += "This method takes:\n\n"
                docStr += '\n'.join(['- ``%s``' % x for x in entry['args']])
                docStr += '\n\n'
            else:
                docStr += "This method takes no arguments.  "

            if 'input' in entry:
                docStr += "This method takes input ``%s``.  " % entry['input']

            if 'output' in entry:
                docStr += "This method gives output ``%s``" % entry['output']

            docStr += '\n\nThis method does a ``%s`` to ``%s``.' % (
                entry['method'].upper(), entry['route'])

            f.__doc__ = docStr

        elif entry['type'] == 'topic-exchange':
            def addTopicExchange(e):
                def topicExchange(self, *args, **kwargs):
                    return self._makeTopicExchange(e, *args, **kwargs)
                return topicExchange

            f = addTopicExchange(entry)

            docStr = 'Generate a routing key pattern for the %s exchange.  ' % entry['exchange']
            docStr += 'This method takes a given routing key as a string or a '
            docStr += 'dictionary.  For each given dictionary key, the corresponding '
            docStr += 'routing key token takes its value.  For routing key tokens '
            docStr += 'which are not specified by the dictionary, the * or # character '
            docStr += 'is used depending on whether or not the key allows multiple words.\n\n'
            docStr += 'This exchange takes the following keys:\n\n'
            docStr += '\n'.join(['- ``%s``' % x['name'] for x in entry['routingKey']])

            f.__doc__ = docStr

        # Give the function the right name
        f.__name__ = str(entry['name'])

        # Add whichever function we created
        attributes[entry['name']] = f

    return type(utils.toStr(name), (RuntimeClient,), attributes)
