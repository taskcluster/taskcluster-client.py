"""This module is used to interact with taskcluster rest apis"""

from __future__ import absolute_import, division, print_function

import logging
import copy
import hashlib
import hmac
import datetime
import calendar
import six

from taskcluster.baseclient import API_CONFIG, config
from taskcluster.runtimeclient import RuntimeClient, createApiClient
import taskcluster.exceptions as exceptions
import taskcluster.utils as utils

log = logging.getLogger(__name__)

_defaultConfig = copy.deepcopy(config)


def createTemporaryCredentials(clientId, accessToken, start, expiry, scopes, name=None):
    """ Create a set of temporary credentials

    clientId: the issuing clientId
    accessToken: the issuer's accessToken
    start: start time of credentials, seconds since epoch
    expiry: expiration time of credentials, seconds since epoch
    scopes: list of scopes granted
    name: credential name (optional)

    Returns a dictionary in the form:
        { 'clientId': str, 'accessToken: str, 'certificate': str}
    """

    now = datetime.datetime.utcnow()
    now = now - datetime.timedelta(minutes=10)  # Subtract 5 minutes for clock drift

    for scope in scopes:
        if not isinstance(scope, six.string_types):
            raise exceptions.TaskclusterFailure('Scope must be string')

    # Credentials can only be valid for 31 days.  I hope that
    # this is validated on the server somehow...

    if expiry - start > datetime.timedelta(days=31):
        raise exceptions.TaskclusterFailure('Only 31 days allowed')

    # We multiply times by 1000 because the auth service is JS and as a result
    # uses milliseconds instead of seconds
    cert = dict(
        version=1,
        scopes=scopes,
        start=calendar.timegm(start.utctimetuple()) * 1000,
        expiry=calendar.timegm(expiry.utctimetuple()) * 1000,
        seed=utils.slugId() + utils.slugId(),
    )

    # if this is a named temporary credential, include the issuer in the certificate
    if name:
        cert['issuer'] = utils.toStr(clientId)

    sig = ['version:' + utils.toStr(cert['version'])]
    if name:
        sig.extend([
            'clientId:' + utils.toStr(name),
            'issuer:' + utils.toStr(clientId),
        ])
    sig.extend([
        'seed:' + utils.toStr(cert['seed']),
        'start:' + utils.toStr(cert['start']),
        'expiry:' + utils.toStr(cert['expiry']),
        'scopes:'
    ] + scopes)
    sigStr = '\n'.join(sig).encode()

    if isinstance(accessToken, six.text_type):
        accessToken = accessToken.encode()
    sig = hmac.new(accessToken, sigStr, hashlib.sha256).digest()

    cert['signature'] = utils.encodeStringForB64Header(sig)

    newToken = hmac.new(accessToken, cert['seed'], hashlib.sha256).digest()
    newToken = utils.makeB64UrlSafe(utils.encodeStringForB64Header(newToken)).replace(b'=', b'')

    return {
        'clientId': name or clientId,
        'accessToken': newToken,
        'certificate': utils.dumpJson(cert),
    }

__all__ = ['createTemporaryCredentials', 'config', 'RuntimeClient', 'createApiClient']
# This has to be done after the Client class is declared
for key, value in API_CONFIG.items():
    # import buildtime generated code
    module = __import__('taskcluster.sync.{key}'.format(key=key), globals(),
                        locals(), [key], 0)
    globals()[key] = getattr(module, key)
    __all__.append(key)
