#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import PurgeCache


class TestPurgeCache(GeneratedTC):
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

    def test_purgeCache(self):
        """TestPurgeCache | PurgeCache.purgeCache
        """
        self.try_function(
            'purgeCache',
            'post',
            argumentNames=['provisionerId', 'workerType', 'payload', ],
        )

    def test_ping(self):
        """TestPurgeCache | PurgeCache.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
