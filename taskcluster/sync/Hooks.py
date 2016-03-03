#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Hooks API Documentation
'''
from __future__ import absolute_import, division, print_function

import logging
import taskcluster.baseclient as baseclient

log = logging.getLogger(__name__)


class Hooks(baseclient.BaseClient):
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
    urls = {
        'listHookGroups': '{baseUrl}/hooks',
        'listHooks': '{baseUrl}/hooks/{hookGroupId}',
        'hook': '{baseUrl}/hooks/{hookGroupId}/{hookId}',
        'getHookStatus': '{baseUrl}/hooks/{hookGroupId}/{hookId}/status',
        'getHookSchedule': '{baseUrl}/hooks/{hookGroupId}/{hookId}/schedule',
        'createHook': '{baseUrl}/hooks/{hookGroupId}/{hookId}',
        'updateHook': '{baseUrl}/hooks/{hookGroupId}/{hookId}',
        'removeHook': '{baseUrl}/hooks/{hookGroupId}/{hookId}',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://hooks.taskcluster.net/v1'
        super(Hooks, self).__init__(*args, **kwargs)

    def listHookGroups(self, signUrl=False):
        '''
        List hook groups

        This endpoint will return a list of all hook groups with at least one hook.

        This method takes no arguments.
        '''
        url = self.urls['listHookGroups'].format(
            baseUrl=self.options['baseUrl'],
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def listHooks(self, hookGroupId, signUrl=False):
        '''
        List hooks in a given group

        This endpoint will return a list of all the hook definitions within a
        given hook group.

        This method takes:
        - ``hookGroupId``
        '''
        url = self.urls['listHooks'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def hook(self, hookGroupId, hookId, signUrl=False):
        '''
        Get hook definition

        This endpoint will return the hook defintion for the given `hookGroupId`
        and hookId.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        url = self.urls['hook'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
            hookId=hookId,
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def getHookStatus(self, hookGroupId, hookId, signUrl=False):
        '''
        Get hook status

        This endpoint will return the current status of the hook.  This represents a
        snapshot in time and may vary from one call to the next.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        url = self.urls['getHookStatus'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
            hookId=hookId,
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def getHookSchedule(self, hookGroupId, hookId, signUrl=False):
        '''
        Get hook schedule

        This endpoint will return the schedule and next scheduled creation time
        for the given hook.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        url = self.urls['getHookSchedule'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
            hookId=hookId,
        )
        if signUrl:
            url = self.buildSignedUrl(url)
        return self._makeHttpRequest('get', url)

    def createHook(self, hookGroupId, hookId, payload):
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
        url = self.urls['createHook'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
            hookId=hookId,
        )
        return self._makeHttpRequest('put', url, payload)

    def updateHook(self, hookGroupId, hookId, payload):
        '''
        Update a hook

        This endpoint will update an existing hook.  All fields except
        `hookGroupId` and `hookId` can be modified.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        url = self.urls['updateHook'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
            hookId=hookId,
        )
        return self._makeHttpRequest('post', url, payload)

    def removeHook(self, hookGroupId, hookId):
        '''
        Delete a hook

        This endpoint will remove a hook definition.

        This method takes:
        - ``hookGroupId``
        - ``hookId``
        '''
        url = self.urls['removeHook'].format(
            baseUrl=self.options['baseUrl'],
            hookGroupId=hookGroupId,
            hookId=hookId,
        )
        return self._makeHttpRequest('delete', url)
