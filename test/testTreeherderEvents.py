#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import TreeherderEvents


class TestTreeherderEvents(GeneratedTC):
    """Test the generated TestTreeherderEvents class.
    """
    testClass = TreeherderEvents

    def test_routes(self):
        """TestTreeherderEvents | all urls match the json baseUrls
        """
        self.route_check('TreeherderEvents')

    def test_routingKeys(self):
        """TestTreeherderEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('TreeherderEvents')

    def test_jobs(self):
        """TestTreeherderEvents | TreeherderEvents.jobs topic exchange
        """
        self.try_topic('jobs', 'jobs')
