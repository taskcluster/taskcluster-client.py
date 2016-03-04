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
    The secrets service, is a simple key/value store for secret data
    guarded by TaskCluster scopes.  It is typically available at
    `secrets.taskcluster.net`.
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
        Create Secret

        Set a secret associated with some key.  If the secret already exists, it is updated instead.

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

        Delete the secret attached to some key.

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

        Read the secret attached to some key.

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

        List the names of all visible secrets.

        This method takes no arguments.
        '''
        route = self.makeRoute('list')
        return await self.makeHttpRequest('get', route)

    async def ping(self):
        '''
        Ping Server

        Documented later...

        **Warning** this api end-point is **not stable**.

        This method takes no arguments.
        '''
        route = self.makeRoute('ping')
        return await self.makeHttpRequest('get', route)
