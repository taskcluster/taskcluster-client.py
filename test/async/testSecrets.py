#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Secrets


class TestAsyncSecrets(AsyncGeneratedTC):
    """Test the generated TestSecrets class.
    """
    testClass = Secrets

    def test_routes(self):
        """TestSecrets | all urls match the json baseUrls
        """
        self.route_check('Secrets')

    def test_routingKeys(self):
        """TestSecrets | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Secrets')

    def test_single_async_set(self):
        """TestAsyncSecrets | Secrets.set single
        """
        self.try_function(
            'set',
            'put',
            argumentNames=['name', 'payload', ],
        )

    def test_multi_async_set(self):
        """TestAsyncSecrets | Secrets.set multi
        """
        self.try_async_function(
            'set',
            'put',
            argumentNames=['name', 'payload', ],
        )

    def test_single_async_remove(self):
        """TestAsyncSecrets | Secrets.remove single
        """
        self.try_function(
            'remove',
            'delete',
            argumentNames=['name', ],
        )

    def test_multi_async_remove(self):
        """TestAsyncSecrets | Secrets.remove multi
        """
        self.try_async_function(
            'remove',
            'delete',
            argumentNames=['name', ],
        )

    def test_single_async_get(self):
        """TestAsyncSecrets | Secrets.get single
        """
        self.try_function(
            'get',
            'get',
            argumentNames=['name', ],
        )

    def test_multi_async_get(self):
        """TestAsyncSecrets | Secrets.get multi
        """
        self.try_async_function(
            'get',
            'get',
            argumentNames=['name', ],
        )

    def test_single_async_list(self):
        """TestAsyncSecrets | Secrets.list single
        """
        self.try_function(
            'list',
            'get',
            argumentNames=[],
        )

    def test_multi_async_list(self):
        """TestAsyncSecrets | Secrets.list multi
        """
        self.try_async_function(
            'list',
            'get',
            argumentNames=[],
        )

    def test_single_async_ping(self):
        """TestAsyncSecrets | Secrets.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncSecrets | Secrets.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
