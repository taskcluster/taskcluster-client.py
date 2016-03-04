#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Hooks


class TestHooks(GeneratedTC):
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

    def test_listHookGroups(self):
        """TestHooks | Hooks.listHookGroups
        """
        self.try_function(
            'listHookGroups',
            'get',
            argumentNames=[],
        )

    def test_listHooks(self):
        """TestHooks | Hooks.listHooks
        """
        self.try_function(
            'listHooks',
            'get',
            argumentNames=['hookGroupId', ],
        )

    def test_hook(self):
        """TestHooks | Hooks.hook
        """
        self.try_function(
            'hook',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_getHookStatus(self):
        """TestHooks | Hooks.getHookStatus
        """
        self.try_function(
            'getHookStatus',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_getHookSchedule(self):
        """TestHooks | Hooks.getHookSchedule
        """
        self.try_function(
            'getHookSchedule',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
        )

    def test_createHook(self):
        """TestHooks | Hooks.createHook
        """
        self.try_function(
            'createHook',
            'put',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
        )

    def test_updateHook(self):
        """TestHooks | Hooks.updateHook
        """
        self.try_function(
            'updateHook',
            'post',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
        )

    def test_removeHook(self):
        """TestHooks | Hooks.removeHook
        """
        self.try_function(
            'removeHook',
            'delete',
            argumentNames=['hookGroupId', 'hookId', ],
        )
