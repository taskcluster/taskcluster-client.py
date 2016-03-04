#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Index


class TestAsyncIndex(AsyncGeneratedTC):
    """Test the generated TestIndex class.
    """
    testClass = Index

    def test_routes(self):
        """TestIndex | all urls match the json baseUrls
        """
        self.route_check('Index')

    def test_routingKeys(self):
        """TestIndex | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Index')

    def test_single_async_findTask(self):
        """TestAsyncIndex | Index.findTask single
        """
        self.try_function(
            'findTask',
            'get',
            argumentNames=['namespace', ],
        )

    def test_multi_async_findTask(self):
        """TestAsyncIndex | Index.findTask multi
        """
        self.try_async_function(
            'findTask',
            'get',
            argumentNames=['namespace', ],
        )

    def test_single_async_listNamespaces(self):
        """TestAsyncIndex | Index.listNamespaces single
        """
        self.try_function(
            'listNamespaces',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_multi_async_listNamespaces(self):
        """TestAsyncIndex | Index.listNamespaces multi
        """
        self.try_async_function(
            'listNamespaces',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_single_async_listTasks(self):
        """TestAsyncIndex | Index.listTasks single
        """
        self.try_function(
            'listTasks',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_multi_async_listTasks(self):
        """TestAsyncIndex | Index.listTasks multi
        """
        self.try_async_function(
            'listTasks',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_single_async_insertTask(self):
        """TestAsyncIndex | Index.insertTask single
        """
        self.try_function(
            'insertTask',
            'put',
            argumentNames=['namespace', 'payload', ],
        )

    def test_multi_async_insertTask(self):
        """TestAsyncIndex | Index.insertTask multi
        """
        self.try_async_function(
            'insertTask',
            'put',
            argumentNames=['namespace', 'payload', ],
        )

    def test_single_async_findArtifactFromTask(self):
        """TestAsyncIndex | Index.findArtifactFromTask single
        """
        self.try_function(
            'findArtifactFromTask',
            'get',
            argumentNames=['namespace', 'name', ],
        )

    def test_multi_async_findArtifactFromTask(self):
        """TestAsyncIndex | Index.findArtifactFromTask multi
        """
        self.try_async_function(
            'findArtifactFromTask',
            'get',
            argumentNames=['namespace', 'name', ],
        )

    def test_single_async_ping(self):
        """TestAsyncIndex | Index.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncIndex | Index.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
