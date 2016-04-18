#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Secrets


class TestSecrets(GeneratedTC):
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

    def test_set(self):
        """TestSecrets | Secrets.set
        """
        self.try_function(
            'set',
            'put',
            argumentNames=['name', 'payload', ],
        )

    def test_remove(self):
        """TestSecrets | Secrets.remove
        """
        self.try_function(
            'remove',
            'delete',
            argumentNames=['name', ],
        )

    def test_get(self):
        """TestSecrets | Secrets.get
        """
        self.try_function(
            'get',
            'get',
            argumentNames=['name', ],
        )

    def test_list(self):
        """TestSecrets | Secrets.list
        """
        self.try_function(
            'list',
            'get',
            argumentNames=[],
        )

    def test_ping(self):
        """TestSecrets | Secrets.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
