#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Secrets


class FakeSecrets(FakeGenerated, Secrets):
    pass


class TestSecrets(GeneratedTC):
    """Test the generated TestSecrets class.
    """
    testClass = FakeSecrets

    def test_urls(self):
        """TestSecrets | all urls match the json baseUrls
        """
        self.url_check('Secrets')

    def test_routingKeys(self):
        """TestSecrets | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Secrets')

    def test_set(self):
        """TestSecrets | Secrets.set unsigned
        """
        self.try_function(
            'set',
            'put',
            argumentNames=['name', 'payload', ],
        )

    def test_remove(self):
        """TestSecrets | Secrets.remove unsigned
        """
        self.try_function(
            'remove',
            'delete',
            argumentNames=['name', ],
        )

    def test_get(self):
        """TestSecrets | Secrets.get unsigned
        """
        self.try_function(
            'get',
            'get',
            argumentNames=['name', ],
        )

    def test_list(self):
        """TestSecrets | Secrets.list unsigned
        """
        self.try_function(
            'list',
            'get',
            argumentNames=[],
        )

    def test_ping(self):
        """TestSecrets | Secrets.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
