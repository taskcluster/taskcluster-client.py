#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Scheduler


class FakeScheduler(FakeGenerated, Scheduler):
    pass


class TestScheduler(GeneratedTC):
    """Test the generated TestScheduler class.
    """
    testClass = FakeScheduler

    def test_urls(self):
        """TestScheduler | all urls match the json baseUrls
        """
        self.url_check('Scheduler')

    def test_routingKeys(self):
        """TestScheduler | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Scheduler')

    def test_createTaskGraph(self):
        """TestScheduler | Scheduler.createTaskGraph unsigned
        """
        self.try_function(
            'createTaskGraph',
            'put',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_extendTaskGraph(self):
        """TestScheduler | Scheduler.extendTaskGraph unsigned
        """
        self.try_function(
            'extendTaskGraph',
            'post',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_status(self):
        """TestScheduler | Scheduler.status unsigned
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_info(self):
        """TestScheduler | Scheduler.info unsigned
        """
        self.try_function(
            'info',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_inspect(self):
        """TestScheduler | Scheduler.inspect unsigned
        """
        self.try_function(
            'inspect',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_inspectTask(self):
        """TestScheduler | Scheduler.inspectTask unsigned
        """
        self.try_function(
            'inspectTask',
            'get',
            argumentNames=['taskGraphId', 'taskId', ],
        )

    def test_ping(self):
        """TestScheduler | Scheduler.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
