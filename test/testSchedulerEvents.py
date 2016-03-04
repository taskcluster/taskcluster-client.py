#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import SchedulerEvents


class TestSchedulerEvents(GeneratedTC):
    """Test the generated TestSchedulerEvents class.
    """
    testClass = SchedulerEvents

    def test_routes(self):
        """TestSchedulerEvents | all urls match the json baseUrls
        """
        self.route_check('SchedulerEvents')

    def test_routingKeys(self):
        """TestSchedulerEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('SchedulerEvents')

    def test_taskGraphRunning(self):
        """TestSchedulerEvents | SchedulerEvents.taskGraphRunning topic exchange
        """
        self.try_topic('taskGraphRunning', 'task-graph-running')

    def test_taskGraphExtended(self):
        """TestSchedulerEvents | SchedulerEvents.taskGraphExtended topic exchange
        """
        self.try_topic('taskGraphExtended', 'task-graph-extended')

    def test_taskGraphBlocked(self):
        """TestSchedulerEvents | SchedulerEvents.taskGraphBlocked topic exchange
        """
        self.try_topic('taskGraphBlocked', 'task-graph-blocked')

    def test_taskGraphFinished(self):
        """TestSchedulerEvents | SchedulerEvents.taskGraphFinished topic exchange
        """
        self.try_topic('taskGraphFinished', 'task-graph-finished')
