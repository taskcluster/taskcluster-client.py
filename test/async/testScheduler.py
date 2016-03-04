#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Scheduler


class TestAsyncScheduler(AsyncGeneratedTC):
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

    def test_single_async_createTaskGraph(self):
        """TestAsyncScheduler | Scheduler.createTaskGraph single
        """
        self.try_function(
            'createTaskGraph',
            'put',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_multi_async_createTaskGraph(self):
        """TestAsyncScheduler | Scheduler.createTaskGraph multi
        """
        self.try_async_function(
            'createTaskGraph',
            'put',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_single_async_extendTaskGraph(self):
        """TestAsyncScheduler | Scheduler.extendTaskGraph single
        """
        self.try_function(
            'extendTaskGraph',
            'post',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_multi_async_extendTaskGraph(self):
        """TestAsyncScheduler | Scheduler.extendTaskGraph multi
        """
        self.try_async_function(
            'extendTaskGraph',
            'post',
            argumentNames=['taskGraphId', 'payload', ],
        )

    def test_single_async_status(self):
        """TestAsyncScheduler | Scheduler.status single
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_multi_async_status(self):
        """TestAsyncScheduler | Scheduler.status multi
        """
        self.try_async_function(
            'status',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_single_async_info(self):
        """TestAsyncScheduler | Scheduler.info single
        """
        self.try_function(
            'info',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_multi_async_info(self):
        """TestAsyncScheduler | Scheduler.info multi
        """
        self.try_async_function(
            'info',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_single_async_inspect(self):
        """TestAsyncScheduler | Scheduler.inspect single
        """
        self.try_function(
            'inspect',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_multi_async_inspect(self):
        """TestAsyncScheduler | Scheduler.inspect multi
        """
        self.try_async_function(
            'inspect',
            'get',
            argumentNames=['taskGraphId', ],
        )

    def test_single_async_inspectTask(self):
        """TestAsyncScheduler | Scheduler.inspectTask single
        """
        self.try_function(
            'inspectTask',
            'get',
            argumentNames=['taskGraphId', 'taskId', ],
        )

    def test_multi_async_inspectTask(self):
        """TestAsyncScheduler | Scheduler.inspectTask multi
        """
        self.try_async_function(
            'inspectTask',
            'get',
            argumentNames=['taskGraphId', 'taskId', ],
        )

    def test_single_async_ping(self):
        """TestAsyncScheduler | Scheduler.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncScheduler | Scheduler.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
