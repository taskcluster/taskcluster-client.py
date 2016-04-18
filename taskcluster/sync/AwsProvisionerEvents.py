#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
AWS Provisioner Pulse Exchanges
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.sync.syncclient import SyncClient

log = logging.getLogger(__name__)


class AwsProvisionerEvents(SyncClient):
    '''
    AWS Provisioner Pulse Exchanges
    Exchanges from the provisioner... more docs later
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/aws-provisioner/v1/exchanges.json'
    routingKeys = {
        'workerTypeCreated': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'workerTypeUpdated': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
        'workerTypeRemoved': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
            },
        ],
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['exchangePrefix'] = 'exchange/taskcluster-aws-provisioner/'
        super(AwsProvisionerEvents, self).__init__(*args, **kwargs)

    def workerTypeCreated(self, routingKeyPattern=None):
        '''
        WorkerType Created Message

        When a new `workerType` is created a message will be published to this
        exchange.

        Generate a routing key pattern for the worker-type-created exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``workerType``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "worker-type-created".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['workerTypeCreated'],
            routingKeyPattern
        )

    def workerTypeUpdated(self, routingKeyPattern=None):
        '''
        WorkerType Updated Message

        When a `workerType` is updated a message will be published to this
        exchange.

        Generate a routing key pattern for the worker-type-updated exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``workerType``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "worker-type-updated".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['workerTypeUpdated'],
            routingKeyPattern
        )

    def workerTypeRemoved(self, routingKeyPattern=None):
        '''
        WorkerType Removed Message

        When a `workerType` is removed a message will be published to this
        exchange.

        Generate a routing key pattern for the worker-type-removed exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``workerType``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "worker-type-removed".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['workerTypeRemoved'],
            routingKeyPattern
        )
