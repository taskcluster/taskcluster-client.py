#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import PurgeCacheEvents


class FakePurgeCacheEvents(FakeGenerated, PurgeCacheEvents):
    pass


class TestPurgeCacheEvents(GeneratedTC):
    """Test the generated TestPurgeCacheEvents class.
    """
    testClass = FakePurgeCacheEvents

    def test_urls(self):
        """TestPurgeCacheEvents | all urls match the json baseUrls
        """
        self.url_check('PurgeCacheEvents')

    def test_routingKeys(self):
        """TestPurgeCacheEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('PurgeCacheEvents')

    def test_purgeCache(self):
        """TestPurgeCacheEvents | PurgeCacheEvents.purgeCache topic exchange
        """
        self.try_topic('purgeCache', 'purge-cache')
