#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Purge Cache API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class PurgeCache(AsyncClient):
    '''
    Purge Cache API Documentation
    The purge-cache service, typically available at
    `purge-cache.taskcluster.net`, is responsible for publishing a pulse
    message for workers, so they can purge cache upon request.

    This document describes the API end-point for publishing the pulse
    message. This is mainly intended to be used by tools.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/purge-cache/v1/api.json'
    routes = {
        'purgeCache': '/purge-cache/{provisionerId}/{workerType}',
        'ping': '/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://purge-cache.taskcluster.net/v1'
        super(PurgeCache, self).__init__(*args, **kwargs)

    async def purgeCache(self, provisionerId, workerType, payload):
        '''
        Purge Worker Cache

        Publish a purge-cache message to purge caches named `cacheName` with
        `provisionerId` and `workerType` in the routing-key. Workers should
        be listening for this message and purge caches when they see it.

        This method takes:
        - ``provisionerId``
        - ``workerType``
        '''
        route = self.makeRoute('purgeCache', replDict={
            'provisionerId': provisionerId,
            'workerType': workerType,
        })
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
