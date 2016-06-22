#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Login API
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class Login(AsyncClient):
    '''
    Login API
    The Login service serves as the interface between external authentication
    systems and TaskCluster credentials.  It acts as the server side of
    https://tools.taskcluster.net.  If you are working on federating logins
    with TaskCluster, this is probably *not* the service you are looking for.
    Instead, use the federated login support in the tools site.

    The API methods described here issue temporary credentials based on
    an assertion.  The assertion identifies the user, usually with an
    email-like string.  This string is then passed through a series of
    authorizers, each of which may supply scopes to be included in the
    credentials. Finally, the service generates temporary credentials based
    on those scopes.

    The generated credentials include scopes to create new, permanent clients
    with names based on the user's identifier.  These credentials are
    periodically scanned for scopes that the user does not posess, and disabled
    if such scopes are discovered.  Thus users can create long-lived credentials
    that are only usable until the user's access level is reduced.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/login/v1/api.json'
    routes = {
        'credentialsFromPersonaAssertion': '/persona',
        'ping': '/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://login.taskcluster.net/v1'
        super(Login, self).__init__(*args, **kwargs)

    async def credentialsFromPersonaAssertion(self, payload):
        '''
        Get TaskCluster credentials given a Persona assertion

        Given an [assertion](https://developer.mozilla.org/en-US/Persona/Quick_setup), return an appropriate
        set of temporary credentials.

        The supplied audience must be on a whitelist of TaskCluster-related
        sites configured in the login service.  This is not a general-purpose
        assertion-verification service!

        This method takes no arguments.
        '''
        route = self.makeRoute('credentialsFromPersonaAssertion')
        return await self.makeHttpRequest('post', route, payload)

    async def ping(self):
        '''
        Ping Server

        Documented later...

        **Warning** this api end-point is **not stable**.

        This method takes no arguments.
        '''
        route = self.makeRoute('ping')
        return await self.makeHttpRequest('get', route)
