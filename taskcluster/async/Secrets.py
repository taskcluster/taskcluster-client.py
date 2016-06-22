#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
TaskCluster Secrets API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class Secrets(AsyncClient):
    '''
    TaskCluster Secrets API Documentation
    The secrets service provides a simple key/value store for small bits of secret
    data.  Access is limited by scopes, so values can be considered secret from
    those who do not have the relevant scopes.

    Secrets also have an expiration date, and once a secret has expired it can no
    longer be read.  This is useful for short-term secrets such as a temporary
    service credential or a one-time signing key.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/secrets/v1/api.json'
    routes = {
        'set': '/secret/{name}',
        'remove': '/secret/{name}',
        'get': '/secret/{name}',
        'list': '/secrets',
        'ping': '/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://secrets.taskcluster.net/v1'
        super(Secrets, self).__init__(*args, **kwargs)

    async def set(self, name, payload):
        '''
        Set Secret

        Set the secret associated with some key.  If the secret already exists, it is
        updated instead.

        This method takes:
        - ``name``
        '''
        route = self.makeRoute('set', replDict={
            'name': name,
        })
        return await self.makeHttpRequest('put', route, payload)

    async def remove(self, name):
        '''
        Delete Secret

        Delete the secret associated with some key.

        This method takes:
        - ``name``
        '''
        route = self.makeRoute('remove', replDict={
            'name': name,
        })
        return await self.makeHttpRequest('delete', route)

    async def get(self, name):
        '''
        Read Secret

        Read the secret associated with some key.  If the secret has recently
        expired, the response code 410 is returned.  If the caller lacks the
        scope necessary to get the secret, the call will fail with a 403 code
        regardless of whether the secret exists.

        This method takes:
        - ``name``
        '''
        route = self.makeRoute('get', replDict={
            'name': name,
        })
        return await self.makeHttpRequest('get', route)

    async def list(self):
        '''
        List Secrets

        List the names of all secrets that you would have access to read. In
        other words, secret name `<X>` will only be returned if a) a secret
        with name `<X>` exists, and b) you posses the scope `secrets:get:<X>`.

        This method takes no arguments.
        '''
        route = self.makeRoute('list')
        return await self.makeHttpRequest('get', route)

    async def ping(self):
        '''
        Ping Server

        Respond without doing anything.  This endpoint is used to check that
        the service is up.

        This method takes no arguments.
        '''
        route = self.makeRoute('ping')
        return await self.makeHttpRequest('get', route)
