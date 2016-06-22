#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import AuthEvents


class TestAuthEvents(GeneratedTC):
    """Test the generated TestAuthEvents class.
    """
    testClass = AuthEvents

    def test_routes(self):
        """TestAuthEvents | all urls match the json baseUrls
        """
        self.route_check('AuthEvents')

    def test_routingKeys(self):
        """TestAuthEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('AuthEvents')

    def test_clientCreated(self):
        """TestAuthEvents | AuthEvents.clientCreated topic exchange
        """
        self.try_topic('clientCreated', 'client-created')

    def test_clientUpdated(self):
        """TestAuthEvents | AuthEvents.clientUpdated topic exchange
        """
        self.try_topic('clientUpdated', 'client-updated')

    def test_clientDeleted(self):
        """TestAuthEvents | AuthEvents.clientDeleted topic exchange
        """
        self.try_topic('clientDeleted', 'client-deleted')

    def test_roleCreated(self):
        """TestAuthEvents | AuthEvents.roleCreated topic exchange
        """
        self.try_topic('roleCreated', 'role-created')

    def test_roleUpdated(self):
        """TestAuthEvents | AuthEvents.roleUpdated topic exchange
        """
        self.try_topic('roleUpdated', 'role-updated')

    def test_roleDeleted(self):
        """TestAuthEvents | AuthEvents.roleDeleted topic exchange
        """
        self.try_topic('roleDeleted', 'role-deleted')
