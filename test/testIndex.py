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

    def test_findTask_unsigned(self):
        """TestIndex | Index.findTask unsigned
        """
        self.try_function(
            'findTask',
            'get',
            argumentNames=['namespace', ],
            signUrl=False
        )

    def test_findTask_signed(self):
        """TestIndex | Index.findTask signed
        """
        self.try_function(
            'findTask',
            'get',
            argumentNames=['namespace', ],
            signUrl=True
        )

    def test_listNamespaces_unsigned(self):
        """TestIndex | Index.listNamespaces unsigned
        """
        self.try_function(
            'listNamespaces',
            'post',
            argumentNames=['namespace', 'payload', ],
            signUrl=False
        )

    def test_listTasks_unsigned(self):
        """TestIndex | Index.listTasks unsigned
        """
        self.try_function(
            'listTasks',
            'post',
            argumentNames=['namespace', 'payload', ],
            signUrl=False
        )

    def test_insertTask_unsigned(self):
        """TestIndex | Index.insertTask unsigned
        """
        self.try_function(
            'insertTask',
            'put',
            argumentNames=['namespace', 'payload', ],
            signUrl=False
        )

    def test_findArtifactFromTask_unsigned(self):
        """TestIndex | Index.findArtifactFromTask unsigned
        """
        self.try_function(
            'findArtifactFromTask',
            'get',
            argumentNames=['namespace', 'name', ],
            signUrl=False
        )

    def test_findArtifactFromTask_signed(self):
        """TestIndex | Index.findArtifactFromTask signed
        """
        self.try_function(
            'findArtifactFromTask',
            'get',
            argumentNames=['namespace', 'name', ],
            signUrl=True
        )

    def test_ping_unsigned(self):
        """TestIndex | Index.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestIndex | Index.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
