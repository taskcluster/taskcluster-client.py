#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Hooks


class TestAsyncHooks(AsyncGeneratedTC):
    """Test the generated TestHooks class.
    """
    testClass = Hooks

    def test_routes(self):
        """TestHooks | all urls match the json baseUrls
        """
        self.route_check('Hooks')

    def test_routingKeys(self):
        """TestHooks | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Hooks')

    def test_single_async_listHookGroups(self):
        """TestAsyncHooks | Hooks.listHookGroups single
        """
        self.try_function(
            'listHookGroups',
            'get',
            argumentNames=[],
        )

    def test_multi_async_listHookGroups(self):
        """TestAsyncHooks | Hooks.listHookGroups multi
        """
        self.try_async_function(
            'listHookGroups',
            'get',
            argumentNames=[],
        )

    def test_single_async_listHooks(self):
        """TestAsyncHooks | Hooks.listHooks single
        """
        self.try_function(
            'listHooks',
            'get',
            argumentNames=['hookGroupId', ],
        )

    def test_multi_async_listHooks(self):
        """TestAsyncHooks | Hooks.listHooks multi
        """
        self.try_async_function(
            'listHooks',
            'get',
            argumentNames=['hookGroupId', ],
        )

    def test_single_async_hook(self):
        """TestAsyncHooks | Hooks.hook single
        """
        self.try_function(
            'hook',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_multi_async_hook(self):
        """TestAsyncHooks | Hooks.hook multi
        """
        self.try_async_function(
            'hook',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_single_async_getHookStatus(self):
        """TestAsyncHooks | Hooks.getHookStatus single
        """
        self.try_function(
            'getHookStatus',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_multi_async_getHookStatus(self):
        """TestAsyncHooks | Hooks.getHookStatus multi
        """
        self.try_async_function(
            'getHookStatus',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_single_async_getHookSchedule(self):
        """TestAsyncHooks | Hooks.getHookSchedule single
        """
        self.try_function(
            'getHookSchedule',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_multi_async_getHookSchedule(self):
        """TestAsyncHooks | Hooks.getHookSchedule multi
        """
        self.try_async_function(
            'getHookSchedule',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_single_async_createHook(self):
        """TestAsyncHooks | Hooks.createHook single
        """
        self.try_function(
            'createHook',
            'put',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
        )

    def test_multi_async_createHook(self):
        """TestAsyncHooks | Hooks.createHook multi
        """
        self.try_async_function(
            'createHook',
            'put',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
        )

    def test_single_async_updateHook(self):
        """TestAsyncHooks | Hooks.updateHook single
        """
        self.try_function(
            'updateHook',
            'post',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
        )

    def test_multi_async_updateHook(self):
        """TestAsyncHooks | Hooks.updateHook multi
        """
        self.try_async_function(
            'updateHook',
            'post',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
        )

    def test_single_async_removeHook(self):
        """TestAsyncHooks | Hooks.removeHook single
        """
        self.try_function(
            'removeHook',
            'delete',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_multi_async_removeHook(self):
        """TestAsyncHooks | Hooks.removeHook multi
        """
        self.try_async_function(
            'removeHook',
            'delete',
            argumentNames=['hookGroupId', 'hookId', ],
        )
