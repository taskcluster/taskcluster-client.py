#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Queue


class FakeQueue(FakeGenerated, Queue):
    pass


class TestQueue(GeneratedTC):
    """Test the generated TestQueue class.
    """
    testClass = FakeQueue

    def test_urls(self):
        """TestQueue | all urls match the json baseUrls
        """
        self.url_check('Queue')

    def test_routingKeys(self):
        """TestQueue | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Queue')

    def test_task_unsigned(self):
        """TestQueue | Queue.task unsigned
        """
        self.try_function(
            'task',
            'get',
            argumentNames=['taskId', ],
            signUrl=False
        )

    def test_task_signed(self):
        """TestQueue | Queue.task signed
        """
        self.try_function(
            'task',
            'get',
            argumentNames=['taskId', ],
            signUrl=True
        )

    def test_status_unsigned(self):
        """TestQueue | Queue.status unsigned
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskId', ],
            signUrl=False
        )

    def test_status_signed(self):
        """TestQueue | Queue.status signed
        """
        self.try_function(
            'status',
            'get',
            argumentNames=['taskId', ],
            signUrl=True
        )

    def test_listTaskGroup_unsigned(self):
        """TestQueue | Queue.listTaskGroup unsigned
        """
        self.try_function(
            'listTaskGroup',
            'get',
            argumentNames=['taskGroupId', ],
            signUrl=False
        )

    def test_listTaskGroup_signed(self):
        """TestQueue | Queue.listTaskGroup signed
        """
        self.try_function(
            'listTaskGroup',
            'get',
            argumentNames=['taskGroupId', ],
            signUrl=True
        )

    def test_createTask_unsigned(self):
        """TestQueue | Queue.createTask unsigned
        """
        self.try_function(
            'createTask',
            'put',
            argumentNames=['taskId', 'payload', ],
            signUrl=False
        )

    def test_defineTask_unsigned(self):
        """TestQueue | Queue.defineTask unsigned
        """
        self.try_function(
            'defineTask',
            'post',
            argumentNames=['taskId', 'payload', ],
            signUrl=False
        )

    def test_scheduleTask_unsigned(self):
        """TestQueue | Queue.scheduleTask unsigned
        """
        self.try_function(
            'scheduleTask',
            'post',
            argumentNames=['taskId', ],
            signUrl=False
        )

    def test_rerunTask_unsigned(self):
        """TestQueue | Queue.rerunTask unsigned
        """
        self.try_function(
            'rerunTask',
            'post',
            argumentNames=['taskId', ],
            signUrl=False
        )

    def test_cancelTask_unsigned(self):
        """TestQueue | Queue.cancelTask unsigned
        """
        self.try_function(
            'cancelTask',
            'post',
            argumentNames=['taskId', ],
            signUrl=False
        )

    def test_pollTaskUrls_unsigned(self):
        """TestQueue | Queue.pollTaskUrls unsigned
        """
        self.try_function(
            'pollTaskUrls',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
            signUrl=False
        )

    def test_pollTaskUrls_signed(self):
        """TestQueue | Queue.pollTaskUrls signed
        """
        self.try_function(
            'pollTaskUrls',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
            signUrl=True
        )

    def test_claimTask_unsigned(self):
        """TestQueue | Queue.claimTask unsigned
        """
        self.try_function(
            'claimTask',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
            signUrl=False
        )

    def test_reclaimTask_unsigned(self):
        """TestQueue | Queue.reclaimTask unsigned
        """
        self.try_function(
            'reclaimTask',
            'post',
            argumentNames=['taskId', 'runId', ],
            signUrl=False
        )

    def test_reportCompleted_unsigned(self):
        """TestQueue | Queue.reportCompleted unsigned
        """
        self.try_function(
            'reportCompleted',
            'post',
            argumentNames=['taskId', 'runId', ],
            signUrl=False
        )

    def test_reportFailed_unsigned(self):
        """TestQueue | Queue.reportFailed unsigned
        """
        self.try_function(
            'reportFailed',
            'post',
            argumentNames=['taskId', 'runId', ],
            signUrl=False
        )

    def test_reportException_unsigned(self):
        """TestQueue | Queue.reportException unsigned
        """
        self.try_function(
            'reportException',
            'post',
            argumentNames=['taskId', 'runId', 'payload', ],
            signUrl=False
        )

    def test_createArtifact_unsigned(self):
        """TestQueue | Queue.createArtifact unsigned
        """
        self.try_function(
            'createArtifact',
            'post',
            argumentNames=['taskId', 'runId', 'name', 'payload', ],
            signUrl=False
        )

    def test_getArtifact_unsigned(self):
        """TestQueue | Queue.getArtifact unsigned
        """
        self.try_function(
            'getArtifact',
            'get',
            argumentNames=['taskId', 'runId', 'name', ],
            signUrl=False
        )

    def test_getArtifact_signed(self):
        """TestQueue | Queue.getArtifact signed
        """
        self.try_function(
            'getArtifact',
            'get',
            argumentNames=['taskId', 'runId', 'name', ],
            signUrl=True
        )

    def test_getLatestArtifact_unsigned(self):
        """TestQueue | Queue.getLatestArtifact unsigned
        """
        self.try_function(
            'getLatestArtifact',
            'get',
            argumentNames=['taskId', 'name', ],
            signUrl=False
        )

    def test_getLatestArtifact_signed(self):
        """TestQueue | Queue.getLatestArtifact signed
        """
        self.try_function(
            'getLatestArtifact',
            'get',
            argumentNames=['taskId', 'name', ],
            signUrl=True
        )

    def test_listArtifacts_unsigned(self):
        """TestQueue | Queue.listArtifacts unsigned
        """
        self.try_function(
            'listArtifacts',
            'get',
            argumentNames=['taskId', 'runId', ],
            signUrl=False
        )

    def test_listArtifacts_signed(self):
        """TestQueue | Queue.listArtifacts signed
        """
        self.try_function(
            'listArtifacts',
            'get',
            argumentNames=['taskId', 'runId', ],
            signUrl=True
        )

    def test_listLatestArtifacts_unsigned(self):
        """TestQueue | Queue.listLatestArtifacts unsigned
        """
        self.try_function(
            'listLatestArtifacts',
            'get',
            argumentNames=['taskId', ],
            signUrl=False
        )

    def test_listLatestArtifacts_signed(self):
        """TestQueue | Queue.listLatestArtifacts signed
        """
        self.try_function(
            'listLatestArtifacts',
            'get',
            argumentNames=['taskId', ],
            signUrl=True
        )

    def test_pendingTasks_unsigned(self):
        """TestQueue | Queue.pendingTasks unsigned
        """
        self.try_function(
            'pendingTasks',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
            signUrl=False
        )

    def test_pendingTasks_signed(self):
        """TestQueue | Queue.pendingTasks signed
        """
        self.try_function(
            'pendingTasks',
            'get',
            argumentNames=['provisionerId', 'workerType', ],
            signUrl=True
        )

    def test_ping_unsigned(self):
        """TestQueue | Queue.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestQueue | Queue.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
