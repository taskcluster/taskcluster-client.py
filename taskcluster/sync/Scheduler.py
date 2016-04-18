#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Task-Graph Scheduler API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.sync.syncclient import SyncClient

log = logging.getLogger(__name__)


class Scheduler(SyncClient):
    '''
    Task-Graph Scheduler API Documentation
    The task-graph scheduler, typically available at
    `scheduler.taskcluster.net`, is responsible for accepting task-graphs and
    scheduling tasks for evaluation by the queue as their dependencies are
    satisfied.

    This document describes API end-points offered by the task-graph
    scheduler. These end-points targets the following audience:
     * Post-commit hooks, that wants to submit task-graphs for testing,
     * End-users, who wants to execute a set of dependent tasks, and
     * Tools, that wants to inspect the state of a task-graph.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/scheduler/v1/api.json'
    routes = {
        'createTaskGraph': '/task-graph/{taskGraphId}',
        'extendTaskGraph': '/task-graph/{taskGraphId}/extend',
        'status': '/task-graph/{taskGraphId}/status',
        'info': '/task-graph/{taskGraphId}/info',
        'inspect': '/task-graph/{taskGraphId}/inspect',
        'inspectTask': '/task-graph/{taskGraphId}/inspect/{taskId}',
        'ping': '/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://scheduler.taskcluster.net/v1'
        super(Scheduler, self).__init__(*args, **kwargs)

    def createTaskGraph(self, taskGraphId, payload):
        '''
        Create new task-graph

        Create a new task-graph, the `status` of the resulting JSON is a
        task-graph status structure, you can find the `taskGraphId` in this
        structure.

        **Referencing required tasks**, it is possible to reference other tasks
        in the task-graph that must be completed successfully before a task is
        scheduled. You just specify the `taskId` in the list of `required` tasks.
        See the example below, where the second task requires the first task.
        ```js
        {
          ...
          tasks: [
            {
              taskId:     "XgvL0qtSR92cIWpcwdGKCA",
              requires:   [],
              ...
            },
            {
              taskId:     "73GsfK62QNKAk2Hg1EEZTQ",
              requires:   ["XgvL0qtSR92cIWpcwdGKCA"],
              task: {
                payload: {
                  env: {
                    DEPENDS_ON:  "XgvL0qtSR92cIWpcwdGKCA"
                  }
                  ...
                }
                ...
              },
              ...
            }
          ]
        }
        ```

        **The `schedulerId` property**, defaults to the `schedulerId` of this
        scheduler in production that is `"task-graph-scheduler"`. This
        property must be either undefined or set to `"task-graph-scheduler"`,
        otherwise the task-graph will be rejected.

        **The `taskGroupId` property**, defaults to the `taskGraphId` of the
        task-graph submitted, and if provided much be the `taskGraphId` of
        the task-graph. Otherwise the task-graph will be rejected.

        **Task-graph scopes**, a task-graph is assigned a set of scopes, just
        like tasks. Tasks within a task-graph cannot have scopes beyond those
        the task-graph has. The task-graph scheduler will execute all requests
        on behalf of a task-graph using the set of scopes assigned to the
        task-graph. Thus, if you are submitting tasks to `my-worker-type` under
        `my-provisioner` it's important that your task-graph has the scope
        required to define tasks for this `provisionerId` and `workerType`.
        (`queue:define-task:..` or `queue:create-task:..`; see the queue for
        details on scopes required). Note, the task-graph does not require
        permissions to schedule the tasks (`queue:schedule-task:..`), as this is
        done with scopes provided by the task-graph scheduler.

        **Task-graph specific routing-keys**, using the `taskGraph.routes`
        property you may define task-graph specific routing-keys. If a task-graph
        has a task-graph specific routing-key: `<route>`, then the poster will
        be required to posses the scope `scheduler:route:<route>`. And when the
        an AMQP message about the task-graph is published the message will be
        CC'ed with the routing-key: `route.<route>`. This is useful if you want
        another component to listen for completed tasks you have posted.

        This method takes:
        - ``taskGraphId``
        '''
        route = self.makeRoute('createTaskGraph', replDict={
            'taskGraphId': taskGraphId,
        })
        return self.makeHttpRequest('put', route, payload)

    def extendTaskGraph(self, taskGraphId, payload):
        '''
        Extend existing task-graph

        Add a set of tasks to an existing task-graph. The request format is very
        similar to the request format for creating task-graphs. But `routes`
        key, `scopes`, `metadata` and `tags` cannot be modified.

        **Referencing required tasks**, just as when task-graphs are created,
        each task has a list of required tasks. It is possible to reference
        all `taskId`s within the task-graph.

        **Safety,** it is only _safe_ to call this API end-point while the
        task-graph being modified is still running. If the task-graph is
        _finished_ or _blocked_, this method will leave the task-graph in this
        state. Hence, it is only truly _safe_ to call this API end-point from
        within a task in the task-graph being modified.

        This method takes:
        - ``taskGraphId``
        '''
        route = self.makeRoute('extendTaskGraph', replDict={
            'taskGraphId': taskGraphId,
        })
        return self.makeHttpRequest('post', route, payload)

    def status(self, taskGraphId):
        '''
        Task Graph Status

        Get task-graph status, this will return the _task-graph status
        structure_. which can be used to check if a task-graph is `running`,
        `blocked` or `finished`.

        **Note**, that `finished` implies successfully completion.

        This method takes:
        - ``taskGraphId``
        '''
        route = self.makeRoute('status', replDict={
            'taskGraphId': taskGraphId,
        })
        return self.makeHttpRequest('get', route)

    def info(self, taskGraphId):
        '''
        Task Graph Information

        Get task-graph information, this includes the _task-graph status
        structure_, along with `metadata` and `tags`, but not information
        about all tasks.

        If you want more detailed information use the `inspectTaskGraph`
        end-point instead.

        This method takes:
        - ``taskGraphId``
        '''
        route = self.makeRoute('info', replDict={
            'taskGraphId': taskGraphId,
        })
        return self.makeHttpRequest('get', route)

    def inspect(self, taskGraphId):
        '''
        Inspect Task Graph

        Inspect a task-graph, this returns all the information the task-graph
        scheduler knows about the task-graph and the state of its tasks.

        **Warning**, some of these fields are borderline internal to the
        task-graph scheduler and we may choose to change or make them internal
        later. Also note that note all of the information is formalized yet.
        The JSON schema will be updated to reflect formalized values, we think
        it's safe to consider the values stable.

        Take these considerations into account when using the API end-point,
        as we do not promise it will remain fully backward compatible in
        the future.

        This method takes:
        - ``taskGraphId``
        '''
        route = self.makeRoute('inspect', replDict={
            'taskGraphId': taskGraphId,
        })
        return self.makeHttpRequest('get', route)

    def inspectTask(self, taskGraphId, taskId):
        '''
        Inspect Task from a Task-Graph

        Inspect a task from a task-graph, this returns all the information the
        task-graph scheduler knows about the specific task.

        **Warning**, some of these fields are borderline internal to the
        task-graph scheduler and we may choose to change or make them internal
        later. Also note that note all of the information is formalized yet.
        The JSON schema will be updated to reflect formalized values, we think
        it's safe to consider the values stable.

        Take these considerations into account when using the API end-point,
        as we do not promise it will remain fully backward compatible in
        the future.

        This method takes:
        - ``taskGraphId``
        - ``taskId``
        '''
        route = self.makeRoute('inspectTask', replDict={
            'taskGraphId': taskGraphId,
            'taskId': taskId,
        })
        return self.makeHttpRequest('get', route)

    def ping(self):
        '''
        Ping Server

        Documented later...

        **Warning** this api end-point is **not stable**.

        This method takes no arguments.
        '''
        route = self.makeRoute('ping')
        return self.makeHttpRequest('get', route)
