#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import PurgeCacheEvents


class TestPurgeCacheEvents(GeneratedTC):
    """Test the generated TestPurgeCacheEvents class.
    """
    testClass = PurgeCacheEvents

    def test_routes(self):
        """TestPurgeCacheEvents | all urls match the json baseUrls
        """
        self.route_check('PurgeCacheEvents')

    def test_routingKeys(self):
        """TestPurgeCacheEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('PurgeCacheEvents')

    def test_purgeCache(self):
        """TestPurgeCacheEvents | PurgeCacheEvents.purgeCache topic exchange
        """
        self.try_topic('purgeCache', 'purge-cache')
