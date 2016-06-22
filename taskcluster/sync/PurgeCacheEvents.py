#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Purge-Cache Exchanges
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.sync.syncclient import SyncClient

log = logging.getLogger(__name__)


class PurgeCacheEvents(SyncClient):
    '''
    Purge-Cache Exchanges
    The purge-cache service, typically available at
    `purge-cache.taskcluster.net`, is responsible for publishing a pulse
    message for workers, so they can purge cache upon request.

    This document describes the exchange offered for workers by the
    cache-purge service.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/purge-cache/v1/exchanges.json'
    routingKeys = {
        'purgeCache': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
                'summary': 'Identifier for the routing-key kind. This is always `\'primary\'` for the formalized routing key.',
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': True,
                'summary': '`provisionerId` under which to purge cache.',
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': True,
                'summary': '`workerType` for which to purge cache.',
            },
        ],
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['exchangePrefix'] = 'exchange/taskcluster-purge-cache/v1/'
        super(PurgeCacheEvents, self).__init__(*args, **kwargs)

    def purgeCache(self, routingKeyPattern=None):
        '''
        Purge Cache Messages

        When a cache purge is requested  a message will be posted on this
        exchange with designated `provisionerId` and `workerType` in the
        routing-key and the name of the `cacheFolder` as payload

        Generate a routing key pattern for the purge-cache exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``provisionerId``
        - ``workerType``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "purge-cache".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['purgeCache'],
            routingKeyPattern
        )
