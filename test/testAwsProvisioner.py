#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import AwsProvisioner


class TestAwsProvisioner(GeneratedTC):
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

    def test_listWorkerTypeSummaries(self):
        """TestAwsProvisioner | AwsProvisioner.listWorkerTypeSummaries
        """
        self.try_function(
            'listWorkerTypeSummaries',
            'get',
            argumentNames=[],
        )

    def test_createWorkerType(self):
        """TestAwsProvisioner | AwsProvisioner.createWorkerType
        """
        self.try_function(
            'createWorkerType',
            'put',
            argumentNames=['workerType', 'payload', ],
        )

    def test_updateWorkerType(self):
        """TestAwsProvisioner | AwsProvisioner.updateWorkerType
        """
        self.try_function(
            'updateWorkerType',
            'post',
            argumentNames=['workerType', 'payload', ],
        )

    def test_workerType(self):
        """TestAwsProvisioner | AwsProvisioner.workerType
        """
        self.try_function(
            'workerType',
            'get',
            argumentNames=['workerType', ],
        )

    def test_removeWorkerType(self):
        """TestAwsProvisioner | AwsProvisioner.removeWorkerType
        """
        self.try_function(
            'removeWorkerType',
            'delete',
            argumentNames=['workerType', ],
        )

    def test_listWorkerTypes(self):
        """TestAwsProvisioner | AwsProvisioner.listWorkerTypes
        """
        self.try_function(
            'listWorkerTypes',
            'get',
            argumentNames=[],
        )

    def test_createSecret(self):
        """TestAwsProvisioner | AwsProvisioner.createSecret
        """
        self.try_function(
            'createSecret',
            'put',
            argumentNames=['token', 'payload', ],
        )

    def test_getSecret(self):
        """TestAwsProvisioner | AwsProvisioner.getSecret
        """
        self.try_function(
            'getSecret',
            'get',
            argumentNames=['token', ],
        )

    def test_instanceStarted(self):
        """TestAwsProvisioner | AwsProvisioner.instanceStarted
        """
        self.try_function(
            'instanceStarted',
            'get',
            argumentNames=['instanceId', 'token', ],
        )

    def test_removeSecret(self):
        """TestAwsProvisioner | AwsProvisioner.removeSecret
        """
        self.try_function(
            'removeSecret',
            'delete',
            argumentNames=['token', ],
        )

    def test_getLaunchSpecs(self):
        """TestAwsProvisioner | AwsProvisioner.getLaunchSpecs
        """
        self.try_function(
            'getLaunchSpecs',
            'get',
            argumentNames=['workerType', ],
        )

    def test_state(self):
        """TestAwsProvisioner | AwsProvisioner.state
        """
        self.try_function(
            'state',
            'get',
            argumentNames=['workerType', ],
        )

    def test_ping(self):
        """TestAwsProvisioner | AwsProvisioner.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_backendStatus(self):
        """TestAwsProvisioner | AwsProvisioner.backendStatus
        """
        self.try_function(
            'backendStatus',
            'get',
            argumentNames=[],
        )
