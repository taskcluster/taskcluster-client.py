#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Login


class TestLogin(GeneratedTC):
    """Test the generated TestLogin class.
    """
    testClass = Login

    def test_routes(self):
        """TestLogin | all urls match the json baseUrls
        """
        self.route_check('Login')

    def test_routingKeys(self):
        """TestLogin | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Login')

    def test_credentialsFromPersonaAssertion(self):
        """TestLogin | Login.credentialsFromPersonaAssertion
        """
        self.try_function(
            'credentialsFromPersonaAssertion',
            'post',
            argumentNames=['payload', ],
        )

    def test_ping(self):
        """TestLogin | Login.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
