#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import AwsProvisioner


class TestAsyncAwsProvisioner(AsyncGeneratedTC):
    """Test the generated TestAwsProvisioner class.
    """
    testClass = AwsProvisioner

    def test_routes(self):
        """TestAwsProvisioner | all urls match the json baseUrls
        """
        self.route_check('AwsProvisioner')

    def test_routingKeys(self):
        """TestAwsProvisioner | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('AwsProvisioner')

    def test_single_async_listWorkerTypeSummaries(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.listWorkerTypeSummaries single
        """
        self.try_function(
            'listWorkerTypeSummaries',
            'get',
            argumentNames=[],
        )

    def test_multi_async_listWorkerTypeSummaries(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.listWorkerTypeSummaries multi
        """
        self.try_async_function(
            'listWorkerTypeSummaries',
            'get',
            argumentNames=[],
        )

    def test_single_async_createWorkerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.createWorkerType single
        """
        self.try_function(
            'createWorkerType',
            'put',
            argumentNames=['workerType', 'payload', ],
        )

    def test_multi_async_createWorkerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.createWorkerType multi
        """
        self.try_async_function(
            'createWorkerType',
            'put',
            argumentNames=['workerType', 'payload', ],
        )

    def test_single_async_updateWorkerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.updateWorkerType single
        """
        self.try_function(
            'updateWorkerType',
            'post',
            argumentNames=['workerType', 'payload', ],
        )

    def test_multi_async_updateWorkerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.updateWorkerType multi
        """
        self.try_async_function(
            'updateWorkerType',
            'post',
            argumentNames=['workerType', 'payload', ],
        )

    def test_single_async_workerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.workerType single
        """
        self.try_function(
            'workerType',
            'get',
            argumentNames=['workerType', ],
        )

    def test_multi_async_workerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.workerType multi
        """
        self.try_async_function(
            'workerType',
            'get',
            argumentNames=['workerType', ],
        )

    def test_single_async_removeWorkerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.removeWorkerType single
        """
        self.try_function(
            'removeWorkerType',
            'delete',
            argumentNames=['workerType', ],
        )

    def test_multi_async_removeWorkerType(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.removeWorkerType multi
        """
        self.try_async_function(
            'removeWorkerType',
            'delete',
            argumentNames=['workerType', ],
        )

    def test_single_async_listWorkerTypes(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.listWorkerTypes single
        """
        self.try_function(
            'listWorkerTypes',
            'get',
            argumentNames=[],
        )

    def test_multi_async_listWorkerTypes(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.listWorkerTypes multi
        """
        self.try_async_function(
            'listWorkerTypes',
            'get',
            argumentNames=[],
        )

    def test_single_async_createSecret(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.createSecret single
        """
        self.try_function(
            'createSecret',
            'put',
            argumentNames=['token', 'payload', ],
        )

    def test_multi_async_createSecret(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.createSecret multi
        """
        self.try_async_function(
            'createSecret',
            'put',
            argumentNames=['token', 'payload', ],
        )

    def test_single_async_getSecret(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.getSecret single
        """
        self.try_function(
            'getSecret',
            'get',
            argumentNames=['token', ],
        )

    def test_multi_async_getSecret(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.getSecret multi
        """
        self.try_async_function(
            'getSecret',
            'get',
            argumentNames=['token', ],
        )

    def test_single_async_instanceStarted(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.instanceStarted single
        """
        self.try_function(
            'instanceStarted',
            'get',
            argumentNames=['instanceId', 'token', ],
        )

    def test_multi_async_instanceStarted(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.instanceStarted multi
        """
        self.try_async_function(
            'instanceStarted',
            'get',
            argumentNames=['instanceId', 'token', ],
        )

    def test_single_async_removeSecret(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.removeSecret single
        """
        self.try_function(
            'removeSecret',
            'delete',
            argumentNames=['token', ],
        )

    def test_multi_async_removeSecret(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.removeSecret multi
        """
        self.try_async_function(
            'removeSecret',
            'delete',
            argumentNames=['token', ],
        )

    def test_single_async_getLaunchSpecs(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.getLaunchSpecs single
        """
        self.try_function(
            'getLaunchSpecs',
            'get',
            argumentNames=['workerType', ],
        )

    def test_multi_async_getLaunchSpecs(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.getLaunchSpecs multi
        """
        self.try_async_function(
            'getLaunchSpecs',
            'get',
            argumentNames=['workerType', ],
        )

    def test_single_async_state(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.state single
        """
        self.try_function(
            'state',
            'get',
            argumentNames=['workerType', ],
        )

    def test_multi_async_state(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.state multi
        """
        self.try_async_function(
            'state',
            'get',
            argumentNames=['workerType', ],
        )

    def test_single_async_ping(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_single_async_backendStatus(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.backendStatus single
        """
        self.try_function(
            'backendStatus',
            'get',
            argumentNames=[],
        )

    def test_multi_async_backendStatus(self):
        """TestAsyncAwsProvisioner | AwsProvisioner.backendStatus multi
        """
        self.try_async_function(
            'backendStatus',
            'get',
            argumentNames=[],
        )
