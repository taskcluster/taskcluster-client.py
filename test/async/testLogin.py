#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Login


class TestAsyncLogin(AsyncGeneratedTC):
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

    def test_single_async_credentialsFromPersonaAssertion(self):
        """TestAsyncLogin | Login.credentialsFromPersonaAssertion single
        """
        self.try_function(
            'credentialsFromPersonaAssertion',
            'post',
            argumentNames=['payload', ],
        )

    def test_multi_async_credentialsFromPersonaAssertion(self):
        """TestAsyncLogin | Login.credentialsFromPersonaAssertion multi
        """
        self.try_async_function(
            'credentialsFromPersonaAssertion',
            'post',
            argumentNames=['payload', ],
        )

    def test_single_async_ping(self):
        """TestAsyncLogin | Login.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncLogin | Login.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
