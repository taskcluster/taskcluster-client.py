#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Taskcluster-treeherder Pulse Exchange
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class TreeherderEvents(AsyncClient):
    '''
    Taskcluster-treeherder Pulse Exchange
    The taskcluster-treeherder service is responsible for processing
    task events published by TaskCluster Queue and producing job messages
    that are consumable by Treeherder.

    This exchange provides that job messages to be consumed by any queue that
    attached to the exchange.  This could be a production Treeheder instance,
    a local development environment, or a custom dashboard.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/taskcluster-treeherder/v1/exchanges.json'
    routingKeys = {
        'jobs': [
            {
                'multipleWords': False,
                'name': 'destination',
                'required': True,
                'summary': 'destination',
            },
            {
                'multipleWords': False,
                'name': 'project',
                'required': True,
                'summary': 'project',
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['exchangePrefix'] = 'exchange/taskcluster-treeherder/v1/'
        super(TreeherderEvents, self).__init__(*args, **kwargs)

    def jobs(self, routingKeyPattern=None):
        '''
        Job Messages

        When a task run is scheduled or resolved, a message is posted to
        this exchange in a Treeherder consumable format.

        Generate a routing key pattern for the jobs exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``destination``
        - ``project``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "jobs".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['jobs'],
            routingKeyPattern
        )
