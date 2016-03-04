#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Hooks API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class Hooks(AsyncClient):
    '''
    Hooks API Documentation
    Hooks are a mechanism for creating tasks in response to events.

    Hooks are identified with a `hookGroupId` and a `hookId`.

    When an event occurs, the resulting task is automatically created.  The
    task is created using the scope `assume:hook-id:<hookGroupId>/<hookId>`,
    which must have scopes to make the createTask call, including satisfying all
    scopes in `task.scopes`.

    Hooks can have a 'schedule' indicating specific times that new tasks should
    be created.  Each schedule is in a simple cron format, per
    https://www.npmjs.com/package/cron-parser.  For example:
     * `["0 0 1 * * *"]` -- daily at 1:00 UTC
     * `["0 0 9,21 * * 1-5", "0 0 12 * * 0,6"]` -- weekdays at 9:00 and 21:00 UTC, weekends at noon
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/hooks/v1/api.json'
    routes = {
        'listHookGroups': '/hooks',
        'listHooks': '/hooks/{hookGroupId}',
        'hook': '/hooks/{hookGroupId}/{hookId}',
        'getHookStatus': '/hooks/{hookGroupId}/{hookId}/status',
        'getHookSchedule': '/hooks/{hookGroupId}/{hookId}/schedule',
        'createHook': '/hooks/{hookGroupId}/{hookId}',
        'updateHook': '/hooks/{hookGroupId}/{hookId}',
        'removeHook': '/hooks/{hookGroupId}/{hookId}',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://hooks.taskcluster.net/v1'
        super(Hooks, self).__init__(*args, **kwargs)

    async def listHookGroups(self):
        '''
        List hook groups

        This endpoint will return a list of all hook groups with at least one hook.

        This method takes no arguments.
        '''
        route = self.makeRoute('listHookGroups')
        return await self.makeHttpRequest('get', route)

    async def listHooks(self, hookGroupId):
        '''
        List hooks in a given group

        This endpoint will return a list of all the hook definitions within a
        given hook group.

        This method takes:
        - ``hookGroupId``
        '''
        route = self.makeRoute('listHooks', replDict={
            'hookGroupId': hookGroupId,
        })
        return await self.makeHttpRequest('get', route)

    async def hook(self, hookGroupId, hookId):
        '''
        Get hook definition

        This endpoint will return the hook defintion for the given `hookGroupId`
        and hookId.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        route = self.makeRoute('hook', replDict={
            'hookGroupId': hookGroupId,
            'hookId': hookId,
        })
        return await self.makeHttpRequest('get', route)

    async def getHookStatus(self, hookGroupId, hookId):
        '''
        Get hook status

        This endpoint will return the current status of the hook.  This represents a
        snapshot in time and may vary from one call to the next.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        route = self.makeRoute('getHookStatus', replDict={
            'hookGroupId': hookGroupId,
            'hookId': hookId,
        })
        return await self.makeHttpRequest('get', route)

    async def getHookSchedule(self, hookGroupId, hookId):
        '''
        Get hook schedule

        This endpoint will return the schedule and next scheduled creation time
        for the given hook.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        route = self.makeRoute('getHookSchedule', replDict={
            'hookGroupId': hookGroupId,
            'hookId': hookId,
        })
        return await self.makeHttpRequest('get', route)

    async def createHook(self, hookGroupId, hookId, payload):
        '''
        Create a hook

        This endpoint will create a new hook.

        The caller's credentials must include the role that will be used to
        create the task.  That role must satisfy task.scopes as well as the
        necessary scopes to add the task to the queue.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        route = self.makeRoute('createHook', replDict={
            'hookGroupId': hookGroupId,
            'hookId': hookId,
        })
        return await self.makeHttpRequest('put', route, payload)

    async def updateHook(self, hookGroupId, hookId, payload):
        '''
        Update a hook

        This endpoint will update an existing hook.  All fields except
        `hookGroupId` and `hookId` can be modified.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        route = self.makeRoute('updateHook', replDict={
            'hookGroupId': hookGroupId,
            'hookId': hookId,
        })
        return await self.makeHttpRequest('post', route, payload)

    async def removeHook(self, hookGroupId, hookId):
        '''
        Delete a hook

        This endpoint will remove a hook definition.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        route = self.makeRoute('removeHook', replDict={
            'hookGroupId': hookGroupId,
            'hookId': hookId,
        })
        return await self.makeHttpRequest('delete', route)
