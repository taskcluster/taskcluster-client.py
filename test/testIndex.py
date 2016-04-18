#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Index


class TestIndex(GeneratedTC):
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

    def test_findTask(self):
        """TestIndex | Index.findTask
        """
        self.try_function(
            'findTask',
            'get',
            argumentNames=['namespace', ],
        )

    def test_listNamespaces(self):
        """TestIndex | Index.listNamespaces
        """
        self.try_function(
            'listNamespaces',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_listTasks(self):
        """TestIndex | Index.listTasks
        """
        self.try_function(
            'listTasks',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_insertTask(self):
        """TestIndex | Index.insertTask
        """
        self.try_function(
            'insertTask',
            'put',
            argumentNames=['namespace', 'payload', ],
        )

    def test_findArtifactFromTask(self):
        """TestIndex | Index.findArtifactFromTask
        """
        self.try_function(
            'findArtifactFromTask',
            'get',
            argumentNames=['namespace', 'name', ],
        )

    def test_ping(self):
        """TestIndex | Index.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
