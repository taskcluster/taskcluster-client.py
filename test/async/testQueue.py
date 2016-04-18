#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Queue


class TestAsyncQueue(AsyncGeneratedTC):
    """Test the generated TestQueue class.
    """
    testClass = Queue

    def test_routes(self):
        """TestQueue | all urls match the json baseUrls
        """
        self.route_check('Queue')

    def test_routingKeys(self):
        """TestQueue | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Queue')

    def test_single_async_task(self):
        """TestAsyncQueue | Queue.task single
        """
        self.try_function(
            'task',
            'get',
            argumentNames=['taskId', ],
        )

    def test_multi_async_task(self):
        """TestAsyncQueue | Queue.task multi
        """
        self.try_async_function(
            'task',
            'get',
            argumentNames=['taskId', ],
        )

    def test_single_async_status(self):
        """TestAsyncQueue | Queue.status single
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskId', ],
        )

    def test_multi_async_status(self):
        """TestAsyncQueue | Queue.status multi
        """
        self.try_async_function(
            'status',
            'get',
            argumentNames=['taskId', ],
        )

    def test_single_async_listTaskGroup(self):
        """TestAsyncQueue | Queue.listTaskGroup single
        """
        self.try_function(
            'listTaskGroup',
            'get',
            argumentNames=['taskGroupId', ],
            validOptions=['continuationToken', 'limit'],
        )

    def test_multi_async_listTaskGroup(self):
        """TestAsyncQueue | Queue.listTaskGroup multi
        """
        self.try_async_function(
            'listTaskGroup',
            'get',
            argumentNames=['taskGroupId', ],
            validOptions=['continuationToken', 'limit'],
        )

    def test_single_async_createTask(self):
        """TestAsyncQueue | Queue.createTask single
        """
        self.try_function(
            'createTask',
            'put',
            argumentNames=['taskId', 'payload', ],
        )

    def test_multi_async_createTask(self):
        """TestAsyncQueue | Queue.createTask multi
        """
        self.try_async_function(
            'createTask',
            'put',
            argumentNames=['taskId', 'payload', ],
        )

    def test_single_async_defineTask(self):
        """TestAsyncQueue | Queue.defineTask single
        """
        self.try_function(
            'defineTask',
            'post',
            argumentNames=['taskId', 'payload', ],
        )

    def test_multi_async_defineTask(self):
        """TestAsyncQueue | Queue.defineTask multi
        """
        self.try_async_function(
            'defineTask',
            'post',
            argumentNames=['taskId', 'payload', ],
        )

    def test_single_async_scheduleTask(self):
        """TestAsyncQueue | Queue.scheduleTask single
        """
        self.try_function(
            'scheduleTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_multi_async_scheduleTask(self):
        """TestAsyncQueue | Queue.scheduleTask multi
        """
        self.try_async_function(
            'scheduleTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_single_async_rerunTask(self):
        """TestAsyncQueue | Queue.rerunTask single
        """
        self.try_function(
            'rerunTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_multi_async_rerunTask(self):
        """TestAsyncQueue | Queue.rerunTask multi
        """
        self.try_async_function(
            'rerunTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_single_async_cancelTask(self):
        """TestAsyncQueue | Queue.cancelTask single
        """
        self.try_function(
            'cancelTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_multi_async_cancelTask(self):
        """TestAsyncQueue | Queue.cancelTask multi
        """
        self.try_async_function(
            'cancelTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_single_async_pollTaskUrls(self):
        """TestAsyncQueue | Queue.pollTaskUrls single
        """
        self.try_function(
            'pollTaskUrls',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
        )

    def test_multi_async_pollTaskUrls(self):
        """TestAsyncQueue | Queue.pollTaskUrls multi
        """
        self.try_async_function(
            'pollTaskUrls',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
        )

    def test_single_async_claimTask(self):
        """TestAsyncQueue | Queue.claimTask single
        """
        self.try_function(
            'claimTask',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
        )

    def test_multi_async_claimTask(self):
        """TestAsyncQueue | Queue.claimTask multi
        """
        self.try_async_function(
            'claimTask',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
        )

    def test_single_async_reclaimTask(self):
        """TestAsyncQueue | Queue.reclaimTask single
        """
        self.try_function(
            'reclaimTask',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_multi_async_reclaimTask(self):
        """TestAsyncQueue | Queue.reclaimTask multi
        """
        self.try_async_function(
            'reclaimTask',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_single_async_reportCompleted(self):
        """TestAsyncQueue | Queue.reportCompleted single
        """
        self.try_function(
            'reportCompleted',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_multi_async_reportCompleted(self):
        """TestAsyncQueue | Queue.reportCompleted multi
        """
        self.try_async_function(
            'reportCompleted',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_single_async_reportFailed(self):
        """TestAsyncQueue | Queue.reportFailed single
        """
        self.try_function(
            'reportFailed',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_multi_async_reportFailed(self):
        """TestAsyncQueue | Queue.reportFailed multi
        """
        self.try_async_function(
            'reportFailed',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_single_async_reportException(self):
        """TestAsyncQueue | Queue.reportException single
        """
        self.try_function(
            'reportException',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
        )

    def test_multi_async_reportException(self):
        """TestAsyncQueue | Queue.reportException multi
        """
        self.try_async_function(
            'reportException',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
        )

    def test_single_async_createArtifact(self):
        """TestAsyncQueue | Queue.createArtifact single
        """
        self.try_function(
            'createArtifact',
            'post',
            argumentNames=['taskId', 'runId', 'name', 'payload', ],
        )

    def test_multi_async_createArtifact(self):
        """TestAsyncQueue | Queue.createArtifact multi
        """
        self.try_async_function(
            'createArtifact',
            'post',
            argumentNames=['taskId', 'runId', 'name', 'payload', ],
        )

    def test_single_async_getArtifact(self):
        """TestAsyncQueue | Queue.getArtifact single
        """
        self.try_function(
            'getArtifact',
            'get',
            argumentNames=['taskId', 'runId', 'name', ],
        )

    def test_multi_async_getArtifact(self):
        """TestAsyncQueue | Queue.getArtifact multi
        """
        self.try_async_function(
            'getArtifact',
            'get',
            argumentNames=['taskId', 'runId', 'name', ],
        )

    def test_single_async_getLatestArtifact(self):
        """TestAsyncQueue | Queue.getLatestArtifact single
        """
        self.try_function(
            'getLatestArtifact',
            'get',
            argumentNames=['taskId', 'name', ],
        )

    def test_multi_async_getLatestArtifact(self):
        """TestAsyncQueue | Queue.getLatestArtifact multi
        """
        self.try_async_function(
            'getLatestArtifact',
            'get',
            argumentNames=['taskId', 'name', ],
        )

    def test_single_async_listArtifacts(self):
        """TestAsyncQueue | Queue.listArtifacts single
        """
        self.try_function(
            'listArtifacts',
            'get',
            argumentNames=['taskId', 'runId', ],
        )

    def test_multi_async_listArtifacts(self):
        """TestAsyncQueue | Queue.listArtifacts multi
        """
        self.try_async_function(
            'listArtifacts',
            'get',
            argumentNames=['taskId', 'runId', ],
        )

    def test_single_async_listLatestArtifacts(self):
        """TestAsyncQueue | Queue.listLatestArtifacts single
        """
        self.try_function(
            'listLatestArtifacts',
            'get',
            argumentNames=['taskId', ],
        )

    def test_multi_async_listLatestArtifacts(self):
        """TestAsyncQueue | Queue.listLatestArtifacts multi
        """
        self.try_async_function(
            'listLatestArtifacts',
            'get',
            argumentNames=['taskId', ],
        )

    def test_single_async_pendingTasks(self):
        """TestAsyncQueue | Queue.pendingTasks single
        """
        self.try_function(
            'pendingTasks',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
        )

    def test_multi_async_pendingTasks(self):
        """TestAsyncQueue | Queue.pendingTasks multi
        """
        self.try_async_function(
            'pendingTasks',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
        )

    def test_single_async_ping(self):
        """TestAsyncQueue | Queue.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncQueue | Queue.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
