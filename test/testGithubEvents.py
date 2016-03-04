#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import GithubEvents


class TestGithubEvents(GeneratedTC):
    """Test the generated TestGithubEvents class.
    """
    testClass = GithubEvents

    def test_routes(self):
        """TestGithubEvents | all urls match the json baseUrls
        """
        self.route_check('GithubEvents')

    def test_routingKeys(self):
        """TestGithubEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('GithubEvents')

    def test_pullRequest(self):
        """TestGithubEvents | GithubEvents.pullRequest topic exchange
        """
        self.try_topic('pullRequest', 'pull-request')

    def test_push(self):
        """TestGithubEvents | GithubEvents.push topic exchange
        """
        self.try_topic('push', 'push')
