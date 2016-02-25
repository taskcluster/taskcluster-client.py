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

    def test_createTaskGraph_unsigned(self):
        """TestScheduler | Scheduler.createTaskGraph unsigned
        """
        self.try_function(
            'createTaskGraph',
            'put',
            argumentNames=['taskGraphId', 'payload', ],
            signUrl=False
        )

    def test_extendTaskGraph_unsigned(self):
        """TestScheduler | Scheduler.extendTaskGraph unsigned
        """
        self.try_function(
            'extendTaskGraph',
            'post',
            argumentNames=['taskGraphId', 'payload', ],
            signUrl=False
        )

    def test_status_unsigned(self):
        """TestScheduler | Scheduler.status unsigned
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskGraphId', ],
            signUrl=False
        )

    def test_status_signed(self):
        """TestScheduler | Scheduler.status signed
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskGraphId', ],
            signUrl=True
        )

    def test_info_unsigned(self):
        """TestScheduler | Scheduler.info unsigned
        """
        self.try_function(
            'info',
            'get',
            argumentNames=['taskGraphId', ],
            signUrl=False
        )

    def test_info_signed(self):
        """TestScheduler | Scheduler.info signed
        """
        self.try_function(
            'info',
            'get',
            argumentNames=['taskGraphId', ],
            signUrl=True
        )

    def test_inspect_unsigned(self):
        """TestScheduler | Scheduler.inspect unsigned
        """
        self.try_function(
            'inspect',
            'get',
            argumentNames=['taskGraphId', ],
            signUrl=False
        )

    def test_inspect_signed(self):
        """TestScheduler | Scheduler.inspect signed
        """
        self.try_function(
            'inspect',
            'get',
            argumentNames=['taskGraphId', ],
            signUrl=True
        )

    def test_inspectTask_unsigned(self):
        """TestScheduler | Scheduler.inspectTask unsigned
        """
        self.try_function(
            'inspectTask',
            'get',
            argumentNames=['taskGraphId', 'taskId', ],
            signUrl=False
        )

    def test_inspectTask_signed(self):
        """TestScheduler | Scheduler.inspectTask signed
        """
        self.try_function(
            'inspectTask',
            'get',
            argumentNames=['taskGraphId', 'taskId', ],
            signUrl=True
        )

    def test_ping_unsigned(self):
        """TestScheduler | Scheduler.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestScheduler | Scheduler.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
