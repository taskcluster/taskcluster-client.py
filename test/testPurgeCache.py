#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import PurgeCache


class FakePurgeCache(FakeGenerated, PurgeCache):
    pass


class TestPurgeCache(GeneratedTC):
    """Test the generated TestPurgeCache class.
    """
    testClass = FakePurgeCache

    def test_urls(self):
        """TestPurgeCache | all urls match the json baseUrls
        """
        self.url_check('PurgeCache')

    def test_routingKeys(self):
        """TestPurgeCache | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('PurgeCache')

    def test_purgeCache_unsigned(self):
        """TestPurgeCache | PurgeCache.purgeCache unsigned
        """
        self.try_function(
            'purgeCache',
            'post',
            argumentNames=['provisionerId', 'workerType', 'payload', ],
            signUrl=False
        )

    def test_ping_unsigned(self):
        """TestPurgeCache | PurgeCache.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestPurgeCache | PurgeCache.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
