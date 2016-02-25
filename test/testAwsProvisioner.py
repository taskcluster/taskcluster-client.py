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

    def test_createWorkerType_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.createWorkerType unsigned
        """
        self.try_function(
            'createWorkerType',
            'put',
            argumentNames=['workerType', 'payload', ],
            signUrl=False
        )

    def test_updateWorkerType_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.updateWorkerType unsigned
        """
        self.try_function(
            'updateWorkerType',
            'post',
            argumentNames=['workerType', 'payload', ],
            signUrl=False
        )

    def test_workerType_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.workerType unsigned
        """
        self.try_function(
            'workerType',
            'get',
            argumentNames=['workerType', ],
            signUrl=False
        )

    def test_workerType_signed(self):
        """TestAwsProvisioner | AwsProvisioner.workerType signed
        """
        self.try_function(
            'workerType',
            'get',
            argumentNames=['workerType', ],
            signUrl=True
        )

    def test_removeWorkerType_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.removeWorkerType unsigned
        """
        self.try_function(
            'removeWorkerType',
            'delete',
            argumentNames=['workerType', ],
            signUrl=False
        )

    def test_listWorkerTypes_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.listWorkerTypes unsigned
        """
        self.try_function(
            'listWorkerTypes',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_listWorkerTypes_signed(self):
        """TestAwsProvisioner | AwsProvisioner.listWorkerTypes signed
        """
        self.try_function(
            'listWorkerTypes',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_createSecret_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.createSecret unsigned
        """
        self.try_function(
            'createSecret',
            'put',
            argumentNames=['token', 'payload', ],
            signUrl=False
        )

    def test_getSecret_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.getSecret unsigned
        """
        self.try_function(
            'getSecret',
            'get',
            argumentNames=['token', ],
            signUrl=False
        )

    def test_getSecret_signed(self):
        """TestAwsProvisioner | AwsProvisioner.getSecret signed
        """
        self.try_function(
            'getSecret',
            'get',
            argumentNames=['token', ],
            signUrl=True
        )

    def test_instanceStarted_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.instanceStarted unsigned
        """
        self.try_function(
            'instanceStarted',
            'get',
            argumentNames=['instanceId', 'token', ],
            signUrl=False
        )

    def test_instanceStarted_signed(self):
        """TestAwsProvisioner | AwsProvisioner.instanceStarted signed
        """
        self.try_function(
            'instanceStarted',
            'get',
            argumentNames=['instanceId', 'token', ],
            signUrl=True
        )

    def test_removeSecret_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.removeSecret unsigned
        """
        self.try_function(
            'removeSecret',
            'delete',
            argumentNames=['token', ],
            signUrl=False
        )

    def test_getLaunchSpecs_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.getLaunchSpecs unsigned
        """
        self.try_function(
            'getLaunchSpecs',
            'get',
            argumentNames=['workerType', ],
            signUrl=False
        )

    def test_getLaunchSpecs_signed(self):
        """TestAwsProvisioner | AwsProvisioner.getLaunchSpecs signed
        """
        self.try_function(
            'getLaunchSpecs',
            'get',
            argumentNames=['workerType', ],
            signUrl=True
        )

    def test_awsState_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.awsState unsigned
        """
        self.try_function(
            'awsState',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_awsState_signed(self):
        """TestAwsProvisioner | AwsProvisioner.awsState signed
        """
        self.try_function(
            'awsState',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_state_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.state unsigned
        """
        self.try_function(
            'state',
            'get',
            argumentNames=['workerType', ],
            signUrl=False
        )

    def test_state_signed(self):
        """TestAwsProvisioner | AwsProvisioner.state signed
        """
        self.try_function(
            'state',
            'get',
            argumentNames=['workerType', ],
            signUrl=True
        )

    def test_ping_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestAwsProvisioner | AwsProvisioner.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_backendStatus_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.backendStatus unsigned
        """
        self.try_function(
            'backendStatus',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_backendStatus_signed(self):
        """TestAwsProvisioner | AwsProvisioner.backendStatus signed
        """
        self.try_function(
            'backendStatus',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_apiReference_unsigned(self):
        """TestAwsProvisioner | AwsProvisioner.apiReference unsigned
        """
        self.try_function(
            'apiReference',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_apiReference_signed(self):
        """TestAwsProvisioner | AwsProvisioner.apiReference signed
        """
        self.try_function(
            'apiReference',
            'get',
            argumentNames=[],
            signUrl=True
        )
