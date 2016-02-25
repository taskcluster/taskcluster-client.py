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

    def test_set_unsigned(self):
        """TestSecrets | Secrets.set unsigned
        """
        self.try_function(
            'set',
            'put',
            argumentNames=['name', 'payload', ],
            signUrl=False
        )

    def test_remove_unsigned(self):
        """TestSecrets | Secrets.remove unsigned
        """
        self.try_function(
            'remove',
            'delete',
            argumentNames=['name', ],
            signUrl=False
        )

    def test_get_unsigned(self):
        """TestSecrets | Secrets.get unsigned
        """
        self.try_function(
            'get',
            'get',
            argumentNames=['name', ],
            signUrl=False
        )

    def test_get_signed(self):
        """TestSecrets | Secrets.get signed
        """
        self.try_function(
            'get',
            'get',
            argumentNames=['name', ],
            signUrl=True
        )

    def test_list_unsigned(self):
        """TestSecrets | Secrets.list unsigned
        """
        self.try_function(
            'list',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_list_signed(self):
        """TestSecrets | Secrets.list signed
        """
        self.try_function(
            'list',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_ping_unsigned(self):
        """TestSecrets | Secrets.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestSecrets | Secrets.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
