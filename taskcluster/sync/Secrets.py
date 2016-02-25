#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
TaskCluster Secrets API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
import taskcluster.baseclient as baseclient

log = logging.getLogger(__name__)


class Secrets(baseclient.BaseClient):
    '''
    TaskCluster Secrets API Documentation
    The secrets service, is a simple key/value store for secret data
    guarded by TaskCluster scopes.  It is typically available at
    `secrets.taskcluster.net`.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/secrets/v1/api.json'
    urls = {
        'set': '{baseUrl}/secret/{name}',
        'remove': '{baseUrl}/secret/{name}',
        'get': '{baseUrl}/secret/{name}',
        'list': '{baseUrl}/secrets',
        'ping': '{baseUrl}/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://secrets.taskcluster.net/v1'
        super(Secrets, self).__init__(*args, **kwargs)

    def set(self, name, payload):
        '''
        Create Secret

        Set a secret associated with some key.  If the secret already exists, it is updated instead.

        This method takes:
        - ``name``
        '''
        url = self.urls['set'].format(
            baseUrl=self.options['baseUrl'],
            name=name,
        )
        return self._makeHttpRequest('put', url, payload)

    def remove(self, name):
        '''
        Delete Secret

        Delete the secret attached to some key.

        This method takes:
        - ``name``
        '''
        url = self.urls['remove'].format(
            baseUrl=self.options['baseUrl'],
            name=name,
        )
        return self._makeHttpRequest('delete', url)

    def get(self, name, signUrl=False):
        '''
        Read Secret

        Read the secret attached to some key.

        This method takes:
        - ``name``
        '''
        url = self.urls['get'].format(
            baseUrl=self.options['baseUrl'],
            name=name,
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def list(self, signUrl=False):
        '''
        List Secrets

        List the names of all visible secrets.

        This method takes no arguments.
        '''
        url = self.urls['list'].format(
            baseUrl=self.options['baseUrl'],
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def ping(self, signUrl=False):
        '''
        Ping Server

        Documented later...
        **Warning** this api end-point is **not stable**.

        This method takes no arguments.
        '''
        url = self.urls['ping'].format(
            baseUrl=self.options['baseUrl'],
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)
