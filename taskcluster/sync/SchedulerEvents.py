#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Scheduler AMQP Exchanges
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.sync.syncclient import SyncClient

log = logging.getLogger(__name__)


class SchedulerEvents(SyncClient):
    '''
    Scheduler AMQP Exchanges
    The scheduler, typically available at `scheduler.taskcluster.net` is
    responsible for accepting task-graphs and schedule tasks on the queue as
    their dependencies are completed successfully.

    This document describes the AMQP exchanges offered by the scheduler,
    which allows third-party listeners to monitor task-graph submission and
    resolution. These exchanges targets the following audience:
     * Reporters, who displays the state of task-graphs or emails people on
       failures, and
     * End-users, who wants notification of completed task-graphs

    **Remark**, the task-graph scheduler will require that the `schedulerId`
    for tasks is set to the `schedulerId` for the task-graph scheduler. In
    production the `schedulerId` is typically `"task-graph-scheduler"`.
    Furthermore, the task-graph scheduler will also require that
    `taskGroupId` is equal to the `taskGraphId`.

    Combined these requirements ensures that `schedulerId` and `taskGroupId`
    have the same position in the routing keys for the queue exchanges.
    See queue documentation for details on queue exchanges. Hence, making
    it easy to listen for all tasks in a given task-graph.

    Note that routing key entries 2 through 7 used for exchanges on the
    task-graph scheduler is hardcoded to `_`. This is done to preserve
    positional equivalence with exchanges offered by the queue.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/scheduler/v1/exchanges.json'
    routingKeys = {
        'taskGraphRunning': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
                'summary': 'Identifier for the routing-key kind. This is always `\'primary\'` for the formalized routing key.',
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
                'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.',
            },
            {
                'multipleWords': False,
                'name': 'taskGraphId',
                'required': True,
                'summary': 'Identifier for the task-graph this message concerns',
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'taskGraphExtended': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
                'summary': 'Identifier for the routing-key kind. This is always `\'primary\'` for the formalized routing key.',
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
                'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.',
            },
            {
                'multipleWords': False,
                'name': 'taskGraphId',
                'required': True,
                'summary': 'Identifier for the task-graph this message concerns',
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'taskGraphBlocked': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
                'summary': 'Identifier for the routing-key kind. This is always `\'primary\'` for the formalized routing key.',
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
                'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.',
            },
            {
                'multipleWords': False,
                'name': 'taskGraphId',
                'required': True,
                'summary': 'Identifier for the task-graph this message concerns',
            },
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'taskGraphFinished': [
            {
                'constant': 'primary',
                'multipleWords': False,
                'name': 'routingKeyKind',
                'required': True,
                'summary': 'Identifier for the routing-key kind. This is always `\'primary\'` for the formalized routing key.',
            },
            {
                'multipleWords': False,
                'name': 'taskId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'runId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerGroup',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'provisionerId',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'workerType',
                'required': False,
                'summary': 'Always takes the value `_`',
            },
            {
                'multipleWords': False,
                'name': 'schedulerId',
                'required': True,
                'summary': 'Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.',
            },
            {
                'multipleWords': False,
                'name': 'taskGraphId',
                'required': True,
                'summary': 'Identifier for the task-graph this message concerns',
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
        self.classOptions['exchangePrefix'] = 'exchange/taskcluster-scheduler/v1/'
        super(SchedulerEvents, self).__init__(*args, **kwargs)

    def taskGraphRunning(self, routingKeyPattern=None):
        '''
        Task-Graph Running Message

        When a task-graph is submitted it immediately starts running and a
        message is posted on this exchange to indicate that a task-graph have
        been submitted.

        Generate a routing key pattern for the task-graph-running exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGraphId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-graph-running".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskGraphRunning'],
            routingKeyPattern
        )

    def taskGraphExtended(self, routingKeyPattern=None):
        '''
        Task-Graph Extended Message

        When a task-graph is extended, that is additional tasks is added to the
        task-graph, a message is posted on this exchange. This is useful if you
        are monitoring a task-graph and what to track states of the individual
        tasks in the task-graph.

        Generate a routing key pattern for the task-graph-extended exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGraphId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-graph-extended".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskGraphExtended'],
            routingKeyPattern
        )

    def taskGraphBlocked(self, routingKeyPattern=None):
        '''
        Task-Graph Blocked Message

        When a task is completed unsuccessfully and all reruns have been
        attempted, the task-graph will not complete successfully and it's
        declared to be _blocked_, by some task that consistently completes
        unsuccessfully.

        When a task-graph becomes blocked a messages is posted to this exchange.
        The message features the `taskId` of the task that caused the task-graph
        to become blocked.

        Generate a routing key pattern for the task-graph-blocked exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGraphId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-graph-blocked".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskGraphBlocked'],
            routingKeyPattern
        )

    def taskGraphFinished(self, routingKeyPattern=None):
        '''
        Task-Graph Finished Message

        When all tasks of a task-graph have completed successfully, the
        task-graph is declared to be finished, and a message is posted to this
        exchange.

        Generate a routing key pattern for the task-graph-finished exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``routingKeyKind``
        - ``taskId``
        - ``runId``
        - ``workerGroup``
        - ``workerId``
        - ``provisionerId``
        - ``workerType``
        - ``schedulerId``
        - ``taskGraphId``
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "task-graph-finished".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['taskGraphFinished'],
            routingKeyPattern
        )
