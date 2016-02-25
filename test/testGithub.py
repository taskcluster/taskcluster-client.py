#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Github


class FakeGithub(FakeGenerated, Github):
    pass


class TestGithub(GeneratedTC):
    """Test the generated TestGithub class.
    """
    testClass = FakeGithub

    def test_urls(self):
        """TestGithub | all urls match the json baseUrls
        """
        self.url_check('Github')

    def test_routingKeys(self):
        """TestGithub | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Github')

    def test_githubWebHookConsumer_unsigned(self):
        """TestGithub | Github.githubWebHookConsumer unsigned
        """
        self.try_function(
            'githubWebHookConsumer',
            'post',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_unsigned(self):
        """TestGithub | Github.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestGithub | Github.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
