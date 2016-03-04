#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
TaskCluster GitHub API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class Github(AsyncClient):
    '''
    TaskCluster GitHub API Documentation
    The github service, typically available at
    `github.taskcluster.net`, is responsible for publishing pulse
    messages in response to GitHub events.

    This document describes the API end-point for consuming GitHub
    web hooks
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/github/v1/api.json'
    routes = {
        'githubWebHookConsumer': '/github',
        'ping': '/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://github.taskcluster.net/v1'
        super(Github, self).__init__(*args, **kwargs)

    async def githubWebHookConsumer(self):
        '''
        Consume GitHub WebHook

        Capture a GitHub event and publish it via pulse, if it's a push
        or pull request.

        This method takes no arguments.
        '''
        route = self.makeRoute('githubWebHookConsumer')
        return await self.makeHttpRequest('post', route)

    async def ping(self):
        '''
        Ping Server

        Documented later...

        **Warning** this api end-point is **not stable**.

        This method takes no arguments.
        '''
        route = self.makeRoute('ping')
        return await self.makeHttpRequest('get', route)
