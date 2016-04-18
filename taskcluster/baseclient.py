"""This module is used to interact with taskcluster rest apis"""

from __future__ import absolute_import, division, print_function

import os
import json
import logging
import copy
import re
import time
import six
from six.moves import urllib

# For finding apis.json
from pkg_resources import resource_string

import mohawk
import mohawk.bewit

import taskcluster.exceptions as exceptions
import taskcluster.utils as utils

log = logging.getLogger(__name__)

API_CONFIG = json.loads(resource_string(__name__, 'apis.json').decode('utf-8'))

# Default configuration
_defaultConfig = config = {
    'credentials': {
        'clientId': os.environ.get('TASKCLUSTER_CLIENT_ID'),
        'accessToken': os.environ.get('TASKCLUSTER_ACCESS_TOKEN'),
        'certificate': os.environ.get('TASKCLUSTER_CERTIFICATE'),
    },
    'maxRetries': 5,
    'signedUrlExpiration': 15 * 60,
}


class BaseClient(object):
    """ Base Class for API Client Classes. Each individual Client class
    needs to set up its own methods for REST endpoints and Topic Exchange
    routing key patterns.
    """
    session = None
    classOptions = {}

    def __init__(self, options=None, session=None, args=(), kwargs=None):
        o = copy.deepcopy(self.classOptions)
        o.update(_defaultConfig)
        if options:
            o.update(options)

        credentials = o.get('credentials')
        if credentials:
            for x in ('accessToken', 'clientId', 'certificate'):
                value = credentials.get(x)
                if value and not isinstance(value, six.binary_type):
                    try:
                        credentials[x] = credentials[x].encode('ascii')
                    except:
                        s = '%s (%s) must be unicode encodable' % (x, credentials[x])
                        raise exceptions.TaskclusterAuthFailure(s)
        self.options = o
        if 'credentials' in o:
            log.debug('credentials key scrubbed from logging output')
        log.debug(dict((k, v) for k, v in o.items() if k != 'credentials'))

        self.createSession(session=session, args=args, kwargs=kwargs)

    def createSession(self, session=None, args=(), kwargs=None):
        pass

    def makeHawkExt(self):
        """ Make an 'ext' for Hawk authentication """
        o = self.options
        c = o.get('credentials', {})
        if c.get('clientId') and c.get('accessToken'):
            ext = {}
            cert = c.get('certificate')
            if cert:
                if six.PY3 and isinstance(cert, six.binary_type):
                    cert = cert.decode()
                if isinstance(cert, six.string_types):
                    cert = json.loads(cert)
                ext['certificate'] = cert

            if 'authorizedScopes' in o:
                ext['authorizedScopes'] = o['authorizedScopes']

            # .encode('base64') inserts a newline, which hawk doesn't
            # like but doesn't strip itself
            return utils.makeB64UrlSafe(utils.encodeStringForB64Header(utils.dumpJson(ext)).strip())
        else:
            return {}

    def _makeTopicExchange(self, exchangeUrl, routingKey, routingKeyPattern):
        if routingKeyPattern is None:
            routingKeyPattern = {}

        data = {
            'exchange': exchangeUrl,
        }

        # If we are passed in a string, we can short-circuit this function
        if isinstance(routingKeyPattern, six.string_types):
            log.debug('Passing through string for topic exchange key')
            data['routingKeyPattern'] = routingKeyPattern
            return data

        if not isinstance(routingKeyPattern, dict):
            errStr = 'routingKeyPattern must eventually be a dict'
            raise exceptions.TaskclusterTopicExchangeFailure(errStr)

        # There is no canonical meaning for the maxSize and required
        # reference entry in the JS client, so we don't try to define
        # them here, even though they sound pretty obvious

        routingKeyParts = []
        for key in routingKey:
            if 'constant' in key:
                value = key['constant']
            elif key['name'] in routingKeyPattern:
                log.debug('Found %s in routing key params', key['name'])
                value = str(routingKeyPattern[key['name']])
                if not key.get('multipleWords') and '.' in value:
                    raise exceptions.TaskclusterTopicExchangeFailure(
                        'Cannot have periods in single word keys')
            else:
                value = '#' if key.get('multipleWords') else '*'
                log.debug('Did not find %s in input params, using %s', key['name'], value)

            routingKeyParts.append(value)

        data['routingKeyPattern'] = '.'.join([utils.toStr(x) for x in routingKeyParts])
        return data

    def makeRoute(self, methodName, route=None, replDict=None):
        """ Given a route like "/task/<taskId>/artifacts" and a mapping like
        {"taskId": "12345"}, return a string like "/task/12345/artifacts"
        """
        if route is None:
            route = self.routes[methodName]
        if replDict is None:
            replDict = {}
        route = re.sub('<(.*?)>', '{\\1}', route)
        for key, value in six.iteritems(replDict):
            replDict[key] = urllib.parse.quote(str(value).encode("utf-8"), '')
            s = '{%s}' % key
            if s not in route:
                raise exceptions.TaskclusterFailure(
                    '%s not found in route for %s (%s)' % (s, methodName, route))
        try:
            route = route.format(**replDict)
        except KeyError:
            raise exceptions.TaskclusterFailure(
                "Error in string formatting %s route %s with %s!" %
                (methodName, route, str(replDict))
            )

        return route.lstrip('/')

    def buildUrl(self, methodName=None, requestUrl=None, replDict=None, **kwargs):
        """Build a tc url.
        We either need a methodName (used to find the route in self.routes) or
        the requestUrl string to use.  If the url needs string formatting, the
        replDict will have the appropriate key/value pairs to format the string
        (e.g. {'clientId': '...'}.
        """
        if not (requestUrl or methodName):
            raise exceptions.TaskclusterFailure(
                "Missing methodName or requestUrl in buildUrl call"
            )
        if requestUrl is None:
            requestUrl = self.makeFullUrl(self.routes[methodName], **kwargs)
        if replDict is None:
            replDict = {}
        for key, value in six.iteritems(replDict):
            replDict[key] = urllib.parse.quote(str(value).encode("utf-8"), '')
        try:
            requestUrl = requestUrl.format(**replDict)
        except KeyError:
            raise exceptions.TaskclusterFailure(
                "Missing string formatting items for url %s: %s" %
                (requestUrl, str(replDict))
            )
        return requestUrl

    def buildSignedUrl(self, requestUrl=None, expiration=None, **kwargs):
        """ Build a signed URL.  This URL contains the credentials needed to access
        a resource.

        **kwargs are passed to buildUrl() if requestUrl isn't set.
        """

        requestUrl = requestUrl or self.buildUrl(**kwargs)
        print(requestUrl)

        expiration = expiration or self.options['signedUrlExpiration']
        expiration = int(time.time() + expiration)  # Mainly so that we throw if it's not a number

        if not self._hasCredentials():
            raise exceptions.TaskclusterAuthFailure('Invalid Hawk Credentials')

        clientId = utils.toStr(self.options['credentials']['clientId'])
        accessToken = utils.toStr(self.options['credentials']['accessToken'])

        def genBewit():
            # We need to fix the output of get_bewit.  It returns a url-safe base64
            # encoded string, which contains a list of tokens separated by '\'.
            # The first one is the clientId, the second is an int, the third is
            # url-safe base64 encoded MAC, the fourth is the ext param.
            # The problem is that the nested url-safe base64 encoded MAC must be
            # base64 (i.e. not url safe) or server-side will complain.

            # id + '\\' + exp + '\\' + mac + '\\' + options.ext;
            resource = mohawk.base.Resource(
                credentials={
                    'id': clientId,
                    'key': accessToken,
                    'algorithm': 'sha256',
                },
                method='GET',
                ext=utils.toStr(self.makeHawkExt()),
                url=requestUrl,
                timestamp=expiration,
                nonce='',
                # content='',
                # content_type='',
            )
            bewit = mohawk.bewit.get_bewit(resource)
            return bewit.rstrip('=')

        bewit = genBewit()

        if not bewit:
            raise exceptions.TaskclusterFailure('Did not receive a bewit')

        u = urllib.parse.urlparse(requestUrl)
        return urllib.parse.urlunparse((
            u.scheme,
            u.netloc,
            u.path,
            u.params,
            u.query + 'bewit=%s' % bewit,
            u.fragment,
        ))

    def _hasCredentials(self):
        """ Return True, if credentials is given """
        cred = self.options.get('credentials')
        return (
            cred and
            'clientId' in cred and
            'accessToken' in cred and
            cred['clientId'] and
            cred['accessToken']
        )

    def makeQueryString(self, options, validOptions=None):
        if not options:
            return ''
        if validOptions:
            validOptionsSet = set(validOptions)
            if not validOptionsSet.issuperset(set(options.keys())):
                raise exceptions.TaskclusterRestFailure(
                    "Invalid options not in validOptions!",
                    str(options), str(validOptions)
                )
        return urllib.parse.urlencode(options)

    def makeFullUrl(self, route, validOptions=None, options=None):
        baseUrl = self.options['baseUrl']
        queryString = ''
        if options:
            queryString = '?' + self.makeQueryString(options, validOptions=validOptions)
        # urljoin ignores the last param of the baseUrl if the base url doesn't end
        # in /.  I wonder if it's better to just do something basic like baseUrl +
        # route instead
        if not baseUrl.endswith('/'):
            baseUrl += '/'
        return urllib.parse.urljoin(baseUrl, route.lstrip('/') + queryString)

    def makeHeaders(self, method, url, payload, hawkExt):
        if self._hasCredentials():
            sender = mohawk.Sender(
                credentials={
                    'id': self.options['credentials']['clientId'],
                    'key': self.options['credentials']['accessToken'],
                    'algorithm': 'sha256',
                },
                ext=hawkExt if hawkExt else {},
                url=url,
                content=payload if payload else '',
                content_type='application/json' if payload else '',
                method=method,
            )

            headers = {'Authorization': sender.request_header}
        else:
            log.debug('Not using hawk!')
            headers = {}
        if payload:
            # Set header for JSON if payload is given, note that we serialize
            # outside this loop.
            headers['Content-Type'] = 'application/json'
        return headers

    def _raiseHttpError(self, status, data, rerr):
        """Helper method to avoid code duplication between AsyncClient and
        SyncClient.
        """
        # Find error message
        message = "Unknown Server Error"
        if isinstance(data, dict):
            message = "{} - {}".format(
                data.get('message'),
                json.dumps(data, indent=4, separators=(',', ': '))
            )
        else:
            if status == 401:
                message = "Authentication Error"
            elif status == 500:
                message = "Internal Server Error"
        # Raise TaskclusterAuthFailure if this is an auth issue
        if status == 401:
            raise exceptions.TaskclusterAuthFailure(
                message,
                status_code=status,
                body=data,
                superExc=rerr
            )
        # Raise TaskclusterRestFailure for all other issues
        raise exceptions.TaskclusterRestFailure(
            message,
            status_code=status,
            body=data,
            superExc=rerr
        )
