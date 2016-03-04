#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Scheduler


class TestScheduler(GeneratedTC):
    """Test the generated TestScheduler class.
    """
    testClass = Scheduler

    def test_routes(self):
        """TestScheduler | all urls match the json baseUrls
        """
        self.route_check('Scheduler')

    def test_routingKeys(self):
        """TestScheduler | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Scheduler')

    def test_createTaskGraph(self):
        """TestScheduler | Scheduler.createTaskGraph
        """
        self.try_function(
            'createTaskGraph',
            'put',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_extendTaskGraph(self):
        """TestScheduler | Scheduler.extendTaskGraph
        """
        self.try_function(
            'extendTaskGraph',
            'post',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_status(self):
        """TestScheduler | Scheduler.status
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_info(self):
        """TestScheduler | Scheduler.info
        """
        self.try_function(
            'info',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_inspect(self):
        """TestScheduler | Scheduler.inspect
        """
        self.try_function(
            'inspect',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_inspectTask(self):
        """TestScheduler | Scheduler.inspectTask
        """
        self.try_function(
            'inspectTask',
            'get',
            argumentNames=['taskGraphId', 'taskId', ],
        )

    def test_ping(self):
        """TestScheduler | Scheduler.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
