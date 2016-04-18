#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import PurgeCache


class TestAsyncPurgeCache(AsyncGeneratedTC):
    """Test the generated TestPurgeCache class.
    """
    testClass = PurgeCache

    def test_routes(self):
        """TestPurgeCache | all urls match the json baseUrls
        """
        self.route_check('PurgeCache')

    def test_routingKeys(self):
        """TestPurgeCache | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('PurgeCache')

    def test_single_async_purgeCache(self):
        """TestAsyncPurgeCache | PurgeCache.purgeCache single
        """
        self.try_function(
            'purgeCache',
            'post',
            argumentNames=['provisionerId', 'workerType', 'payload', ],
        )

    def test_multi_async_purgeCache(self):
        """TestAsyncPurgeCache | PurgeCache.purgeCache multi
        """
        self.try_async_function(
            'purgeCache',
            'post',
            argumentNames=['provisionerId', 'workerType', 'payload', ],
        )

    def test_single_async_ping(self):
        """TestAsyncPurgeCache | PurgeCache.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncPurgeCache | PurgeCache.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
