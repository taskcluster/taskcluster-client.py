#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import AwsProvisionerEvents


class TestAwsProvisionerEvents(GeneratedTC):
    """Test the generated TestAwsProvisionerEvents class.
    """
    testClass = AwsProvisionerEvents

    def test_routes(self):
        """TestAwsProvisionerEvents | all urls match the json baseUrls
        """
        self.route_check('AwsProvisionerEvents')

    def test_routingKeys(self):
        """TestAwsProvisionerEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('AwsProvisionerEvents')

    def test_workerTypeCreated(self):
        """TestAwsProvisionerEvents | AwsProvisionerEvents.workerTypeCreated topic exchange
        """
        self.try_topic('workerTypeCreated', 'worker-type-created')

    def test_workerTypeUpdated(self):
        """TestAwsProvisionerEvents | AwsProvisionerEvents.workerTypeUpdated topic exchange
        """
        self.try_topic('workerTypeUpdated', 'worker-type-updated')

    def test_workerTypeRemoved(self):
        """TestAwsProvisionerEvents | AwsProvisionerEvents.workerTypeRemoved topic exchange
        """
        self.try_topic('workerTypeRemoved', 'worker-type-removed')
