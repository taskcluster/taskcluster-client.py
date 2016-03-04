#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Index


class FakeIndex(FakeGenerated, Index):
    pass


class TestIndex(GeneratedTC):
    """Test the generated TestIndex class.
    """
    testClass = FakeIndex

    def test_urls(self):
        """TestIndex | all urls match the json baseUrls
        """
        self.url_check('Index')

    def test_routingKeys(self):
        """TestIndex | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Index')

    def test_findTask(self):
        """TestIndex | Index.findTask unsigned
        """
        self.try_function(
            'findTask',
            'get',
            argumentNames=['namespace', ],
        )

    def test_listNamespaces(self):
        """TestIndex | Index.listNamespaces unsigned
        """
        self.try_function(
            'listNamespaces',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_listTasks(self):
        """TestIndex | Index.listTasks unsigned
        """
        self.try_function(
            'listTasks',
            'post',
            argumentNames=['namespace', 'payload', ],
        )

    def test_insertTask(self):
        """TestIndex | Index.insertTask unsigned
        """
        self.try_function(
            'insertTask',
            'put',
            argumentNames=['namespace', 'payload', ],
        )

    def test_findArtifactFromTask(self):
        """TestIndex | Index.findArtifactFromTask unsigned
        """
        self.try_function(
            'findArtifactFromTask',
            'get',
            argumentNames=['namespace', 'name', ],
        )

    def test_ping(self):
        """TestIndex | Index.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
