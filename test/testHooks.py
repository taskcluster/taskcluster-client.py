#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Hooks


class FakeHooks(FakeGenerated, Hooks):
    pass


class TestHooks(GeneratedTC):
    """Test the generated TestHooks class.
    """
    testClass = FakeHooks

    def test_urls(self):
        """TestHooks | all urls match the json baseUrls
        """
        self.url_check('Hooks')

    def test_routingKeys(self):
        """TestHooks | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Hooks')

    def test_listHookGroups_unsigned(self):
        """TestHooks | Hooks.listHookGroups unsigned
        """
        self.try_function(
            'listHookGroups',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_listHookGroups_signed(self):
        """TestHooks | Hooks.listHookGroups signed
        """
        self.try_function(
            'listHookGroups',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_listHooks_unsigned(self):
        """TestHooks | Hooks.listHooks unsigned
        """
        self.try_function(
            'listHooks',
            'get',
            argumentNames=['hookGroupId', ],
            signUrl=False
        )

    def test_listHooks_signed(self):
        """TestHooks | Hooks.listHooks signed
        """
        self.try_function(
            'listHooks',
            'get',
            argumentNames=['hookGroupId', ],
            signUrl=True
        )

    def test_hook_unsigned(self):
        """TestHooks | Hooks.hook unsigned
        """
        self.try_function(
            'hook',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=False
        )

    def test_hook_signed(self):
        """TestHooks | Hooks.hook signed
        """
        self.try_function(
            'hook',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=True
        )

    def test_getHookStatus_unsigned(self):
        """TestHooks | Hooks.getHookStatus unsigned
        """
        self.try_function(
            'getHookStatus',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=False
        )

    def test_getHookStatus_signed(self):
        """TestHooks | Hooks.getHookStatus signed
        """
        self.try_function(
            'getHookStatus',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=True
        )

    def test_getHookSchedule_unsigned(self):
        """TestHooks | Hooks.getHookSchedule unsigned
        """
        self.try_function(
            'getHookSchedule',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=False
        )

    def test_getHookSchedule_signed(self):
        """TestHooks | Hooks.getHookSchedule signed
        """
        self.try_function(
            'getHookSchedule',
            'get',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=True
        )

    def test_createHook_unsigned(self):
        """TestHooks | Hooks.createHook unsigned
        """
        self.try_function(
            'createHook',
            'put',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
            signUrl=False
        )

    def test_updateHook_unsigned(self):
        """TestHooks | Hooks.updateHook unsigned
        """
        self.try_function(
            'updateHook',
            'post',
            argumentNames=['hookGroupId', 'hookId', 'payload', ],
            signUrl=False
        )

    def test_removeHook_unsigned(self):
        """TestHooks | Hooks.removeHook unsigned
        """
        self.try_function(
            'removeHook',
            'delete',
            argumentNames=['hookGroupId', 'hookId', ],
            signUrl=False
        )
