#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.base import GeneratedTC
from taskcluster.sync import Auth


class TestAuth(GeneratedTC):
    """Test the generated TestAuth class.
    """
    testClass = Auth

    def test_routes(self):
        """TestAuth | all urls match the json baseUrls
        """
        self.route_check('Auth')

    def test_routingKeys(self):
        """TestAuth | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Auth')

    def test_listClients(self):
        """TestAuth | Auth.listClients
        """
        self.try_function(
            'listClients',
            'get',
            argumentNames=[],
            validOptions=['prefix'],
        )

    def test_client(self):
        """TestAuth | Auth.client
        """
        self.try_function(
            'client',
            'get',
            argumentNames=['clientId', ],
        )

    def test_createClient(self):
        """TestAuth | Auth.createClient
        """
        self.try_function(
            'createClient',
            'put',
            argumentNames=['clientId', 'payload', ],
        )

    def test_resetAccessToken(self):
        """TestAuth | Auth.resetAccessToken
        """
        self.try_function(
            'resetAccessToken',
            'post',
            argumentNames=['clientId', ],
        )

    def test_updateClient(self):
        """TestAuth | Auth.updateClient
        """
        self.try_function(
            'updateClient',
            'post',
            argumentNames=['clientId', 'payload', ],
        )

    def test_enableClient(self):
        """TestAuth | Auth.enableClient
        """
        self.try_function(
            'enableClient',
            'post',
            argumentNames=['clientId', ],
        )

    def test_disableClient(self):
        """TestAuth | Auth.disableClient
        """
        self.try_function(
            'disableClient',
            'post',
            argumentNames=['clientId', ],
        )

    def test_deleteClient(self):
        """TestAuth | Auth.deleteClient
        """
        self.try_function(
            'deleteClient',
            'delete',
            argumentNames=['clientId', ],
        )

    def test_listRoles(self):
        """TestAuth | Auth.listRoles
        """
        self.try_function(
            'listRoles',
            'get',
            argumentNames=[],
        )

    def test_role(self):
        """TestAuth | Auth.role
        """
        self.try_function(
            'role',
            'get',
            argumentNames=['roleId', ],
        )

    def test_createRole(self):
        """TestAuth | Auth.createRole
        """
        self.try_function(
            'createRole',
            'put',
            argumentNames=['roleId', 'payload', ],
        )

    def test_updateRole(self):
        """TestAuth | Auth.updateRole
        """
        self.try_function(
            'updateRole',
            'post',
            argumentNames=['roleId', 'payload', ],
        )

    def test_deleteRole(self):
        """TestAuth | Auth.deleteRole
        """
        self.try_function(
            'deleteRole',
            'delete',
            argumentNames=['roleId', ],
        )

    def test_expandScopes(self):
        """TestAuth | Auth.expandScopes
        """
        self.try_function(
            'expandScopes',
            'get',
            argumentNames=['payload', ],
        )

    def test_currentScopes(self):
        """TestAuth | Auth.currentScopes
        """
        self.try_function(
            'currentScopes',
            'get',
            argumentNames=[],
        )

    def test_awsS3Credentials(self):
        """TestAuth | Auth.awsS3Credentials
        """
        self.try_function(
            'awsS3Credentials',
            'get',
            argumentNames=['level', 'bucket', 'prefix', ],
        )

    def test_azureTableSAS(self):
        """TestAuth | Auth.azureTableSAS
        """
        self.try_function(
            'azureTableSAS',
            'get',
            argumentNames=['account', 'table', ],
        )

    def test_sentryDSN(self):
        """TestAuth | Auth.sentryDSN
        """
        self.try_function(
            'sentryDSN',
            'get',
            argumentNames=['project', ],
        )

    def test_statsumToken(self):
        """TestAuth | Auth.statsumToken
        """
        self.try_function(
            'statsumToken',
            'get',
            argumentNames=['project', ],
        )

    def test_authenticateHawk(self):
        """TestAuth | Auth.authenticateHawk
        """
        self.try_function(
            'authenticateHawk',
            'post',
            argumentNames=['payload', ],
        )

    def test_testAuthenticate(self):
        """TestAuth | Auth.testAuthenticate
        """
        self.try_function(
            'testAuthenticate',
            'post',
            argumentNames=['payload', ],
        )

    def test_testAuthenticateGet(self):
        """TestAuth | Auth.testAuthenticateGet
        """
        self.try_function(
            'testAuthenticateGet',
            'get',
            argumentNames=[],
        )

    def test_ping(self):
        """TestAuth | Auth.ping
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )
