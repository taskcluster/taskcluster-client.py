#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Github


class TestGithub(GeneratedTC):
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

    def test_githubWebHookConsumer(self):
        """TestGithub | Github.githubWebHookConsumer
        """
        self.try_function(
            'githubWebHookConsumer',
            'post',
            argumentNames=[],
        )

    def test_ping(self):
        """TestGithub | Github.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
