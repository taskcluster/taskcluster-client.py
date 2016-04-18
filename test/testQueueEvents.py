#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import QueueEvents


class TestQueueEvents(GeneratedTC):
    """Test the generated TestQueueEvents class.
    """
    testClass = QueueEvents

    def test_routes(self):
        """TestQueueEvents | all urls match the json baseUrls
        """
        self.route_check('QueueEvents')

    def test_routingKeys(self):
        """TestQueueEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('QueueEvents')

    def test_taskDefined(self):
        """TestQueueEvents | QueueEvents.taskDefined topic exchange
        """
        self.try_topic('taskDefined', 'task-defined')

    def test_taskPending(self):
        """TestQueueEvents | QueueEvents.taskPending topic exchange
        """
        self.try_topic('taskPending', 'task-pending')

    def test_taskRunning(self):
        """TestQueueEvents | QueueEvents.taskRunning topic exchange
        """
        self.try_topic('taskRunning', 'task-running')

    def test_artifactCreated(self):
        """TestQueueEvents | QueueEvents.artifactCreated topic exchange
        """
        self.try_topic('artifactCreated', 'artifact-created')

    def test_taskCompleted(self):
        """TestQueueEvents | QueueEvents.taskCompleted topic exchange
        """
        self.try_topic('taskCompleted', 'task-completed')

    def test_taskFailed(self):
        """TestQueueEvents | QueueEvents.taskFailed topic exchange
        """
        self.try_topic('taskFailed', 'task-failed')

    def test_taskException(self):
        """TestQueueEvents | QueueEvents.taskException topic exchange
        """
        self.try_topic('taskException', 'task-exception')
