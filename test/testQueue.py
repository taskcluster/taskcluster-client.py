#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Queue


class TestQueue(GeneratedTC):
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

    def test_task(self):
        """TestQueue | Queue.task
        """
        self.try_function(
            'task',
            'get',
            argumentNames=['taskId', ],
        )

    def test_status(self):
        """TestQueue | Queue.status
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskId', ],
        )

    def test_listTaskGroup(self):
        """TestQueue | Queue.listTaskGroup
        """
        self.try_function(
            'listTaskGroup',
            'get',
            argumentNames=['taskGroupId', ],
            validOptions=['continuationToken', 'limit'],
        )

    def test_listDependentTasks(self):
        """TestQueue | Queue.listDependentTasks
        """
        self.try_function(
            'listDependentTasks',
            'get',
            argumentNames=['taskId', ],
            validOptions=['continuationToken', 'limit'],
        )

    def test_createTask(self):
        """TestQueue | Queue.createTask
        """
        self.try_function(
            'createTask',
            'put',
            argumentNames=['taskId', 'payload', ],
        )

    def test_defineTask(self):
        """TestQueue | Queue.defineTask
        """
        self.try_function(
            'defineTask',
            'post',
            argumentNames=['taskId', 'payload', ],
        )

    def test_scheduleTask(self):
        """TestQueue | Queue.scheduleTask
        """
        self.try_function(
            'scheduleTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_rerunTask(self):
        """TestQueue | Queue.rerunTask
        """
        self.try_function(
            'rerunTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_cancelTask(self):
        """TestQueue | Queue.cancelTask
        """
        self.try_function(
            'cancelTask',
            'post',
            argumentNames=['taskId', ],
        )

    def test_pollTaskUrls(self):
        """TestQueue | Queue.pollTaskUrls
        """
        self.try_function(
            'pollTaskUrls',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
        )

    def test_claimTask(self):
        """TestQueue | Queue.claimTask
        """
        self.try_function(
            'claimTask',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
        )

    def test_reclaimTask(self):
        """TestQueue | Queue.reclaimTask
        """
        self.try_function(
            'reclaimTask',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_reportCompleted(self):
        """TestQueue | Queue.reportCompleted
        """
        self.try_function(
            'reportCompleted',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_reportFailed(self):
        """TestQueue | Queue.reportFailed
        """
        self.try_function(
            'reportFailed',
            'post',
            argumentNames=['taskId', 'runId', ],
        )

    def test_reportException(self):
        """TestQueue | Queue.reportException
        """
        self.try_function(
            'reportException',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
        )

    def test_createArtifact(self):
        """TestQueue | Queue.createArtifact
        """
        self.try_function(
            'createArtifact',
            'post',
            argumentNames=['taskId', 'runId', 'name', 'payload', ],
        )

    def test_getArtifact(self):
        """TestQueue | Queue.getArtifact
        """
        self.try_function(
            'getArtifact',
            'get',
            argumentNames=['taskId', 'runId', 'name', ],
        )

    def test_getLatestArtifact(self):
        """TestQueue | Queue.getLatestArtifact
        """
        self.try_function(
            'getLatestArtifact',
            'get',
            argumentNames=['taskId', 'name', ],
        )

    def test_listArtifacts(self):
        """TestQueue | Queue.listArtifacts
        """
        self.try_function(
            'listArtifacts',
            'get',
            argumentNames=['taskId', 'runId', ],
            validOptions=['continuationToken', 'limit'],
        )

    def test_listLatestArtifacts(self):
        """TestQueue | Queue.listLatestArtifacts
        """
        self.try_function(
            'listLatestArtifacts',
            'get',
            argumentNames=['taskId', ],
            validOptions=['continuationToken', 'limit'],
        )

    def test_pendingTasks(self):
        """TestQueue | Queue.pendingTasks
        """
        self.try_function(
            'pendingTasks',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
        )

    def test_ping(self):
        """TestQueue | Queue.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
