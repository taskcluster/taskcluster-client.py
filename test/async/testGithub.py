#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Github


class TestAsyncGithub(AsyncGeneratedTC):
    """Test the generated TestGithub class.
    """
    testClass = Github

    def test_routes(self):
        """TestGithub | all urls match the json baseUrls
        """
        self.route_check('Github')

    def test_routingKeys(self):
        """TestGithub | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Github')

    def test_single_async_githubWebHookConsumer(self):
        """TestAsyncGithub | Github.githubWebHookConsumer single
        """
        self.try_function(
            'githubWebHookConsumer',
            'post',
            argumentNames=[],
        )

    def test_multi_async_githubWebHookConsumer(self):
        """TestAsyncGithub | Github.githubWebHookConsumer multi
        """
        self.try_async_function(
            'githubWebHookConsumer',
            'post',
            argumentNames=[],
        )

    def test_single_async_ping(self):
        """TestAsyncGithub | Github.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncGithub | Github.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
