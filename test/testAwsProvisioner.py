#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import AwsProvisioner


class FakeAwsProvisioner(FakeGenerated, AwsProvisioner):
    pass


class TestAwsProvisioner(GeneratedTC):
    """Test the generated TestAwsProvisioner class.
    """
    testClass = FakeAwsProvisioner

    def test_urls(self):
        """TestAwsProvisioner | all urls match the json baseUrls
        """
        self.url_check('AwsProvisioner')

    def test_routingKeys(self):
        """TestAwsProvisioner | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('AwsProvisioner')

    def test_createWorkerType(self):
        """TestAwsProvisioner | AwsProvisioner.createWorkerType unsigned
        """
        self.try_function(
            'createWorkerType',
            'put',
            argumentNames=['workerType', 'payload', ],
        )

    def test_updateWorkerType(self):
        """TestAwsProvisioner | AwsProvisioner.updateWorkerType unsigned
        """
        self.try_function(
            'updateWorkerType',
            'post',
            argumentNames=['workerType', 'payload', ],
        )

    def test_workerType(self):
        """TestAwsProvisioner | AwsProvisioner.workerType unsigned
        """
        self.try_function(
            'workerType',
            'get',
            argumentNames=['workerType', ],
        )

    def test_removeWorkerType(self):
        """TestAwsProvisioner | AwsProvisioner.removeWorkerType unsigned
        """
        self.try_function(
            'removeWorkerType',
            'delete',
            argumentNames=['workerType', ],
        )

    def test_listWorkerTypes(self):
        """TestAwsProvisioner | AwsProvisioner.listWorkerTypes unsigned
        """
        self.try_function(
            'listWorkerTypes',
            'get',
            argumentNames=[],
        )

    def test_createSecret(self):
        """TestAwsProvisioner | AwsProvisioner.createSecret unsigned
        """
        self.try_function(
            'createSecret',
            'put',
            argumentNames=['token', 'payload', ],
        )

    def test_getSecret(self):
        """TestAwsProvisioner | AwsProvisioner.getSecret unsigned
        """
        self.try_function(
            'getSecret',
            'get',
            argumentNames=['token', ],
        )

    def test_instanceStarted(self):
        """TestAwsProvisioner | AwsProvisioner.instanceStarted unsigned
        """
        self.try_function(
            'instanceStarted',
            'get',
            argumentNames=['instanceId', 'token', ],
        )

    def test_removeSecret(self):
        """TestAwsProvisioner | AwsProvisioner.removeSecret unsigned
        """
        self.try_function(
            'removeSecret',
            'delete',
            argumentNames=['token', ],
        )

    def test_getLaunchSpecs(self):
        """TestAwsProvisioner | AwsProvisioner.getLaunchSpecs unsigned
        """
        self.try_function(
            'getLaunchSpecs',
            'get',
            argumentNames=['workerType', ],
        )

    def test_awsState(self):
        """TestAwsProvisioner | AwsProvisioner.awsState unsigned
        """
        self.try_function(
            'awsState',
            'get',
            argumentNames=[],
        )

    def test_state(self):
        """TestAwsProvisioner | AwsProvisioner.state unsigned
        """
        self.try_function(
            'state',
            'get',
            argumentNames=['workerType', ],
        )

    def test_ping(self):
        """TestAwsProvisioner | AwsProvisioner.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_backendStatus(self):
        """TestAwsProvisioner | AwsProvisioner.backendStatus unsigned
        """
        self.try_function(
            'backendStatus',
            'get',
            argumentNames=[],
        )

    def test_apiReference(self):
        """TestAwsProvisioner | AwsProvisioner.apiReference unsigned
        """
        self.try_function(
            'apiReference',
            'get',
            argumentNames=[],
        )
