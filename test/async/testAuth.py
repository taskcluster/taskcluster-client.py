#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from test.async import AsyncGeneratedTC
from taskcluster.async import Auth


class TestAsyncAuth(AsyncGeneratedTC):
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

    def test_single_async_listClients(self):
        """TestAsyncAuth | Auth.listClients single
        """
        self.try_function(
            'listClients',
            'get',
            argumentNames=[],
            validOptions=['prefix'],
        )

    def test_multi_async_listClients(self):
        """TestAsyncAuth | Auth.listClients multi
        """
        self.try_async_function(
            'listClients',
            'get',
            argumentNames=[],
            validOptions=['prefix'],
        )

    def test_single_async_client(self):
        """TestAsyncAuth | Auth.client single
        """
        self.try_function(
            'client',
            'get',
            argumentNames=['clientId', ],
        )

    def test_multi_async_client(self):
        """TestAsyncAuth | Auth.client multi
        """
        self.try_async_function(
            'client',
            'get',
            argumentNames=['clientId', ],
        )

    def test_single_async_createClient(self):
        """TestAsyncAuth | Auth.createClient single
        """
        self.try_function(
            'createClient',
            'put',
            argumentNames=['clientId', 'payload', ],
        )

    def test_multi_async_createClient(self):
        """TestAsyncAuth | Auth.createClient multi
        """
        self.try_async_function(
            'createClient',
            'put',
            argumentNames=['clientId', 'payload', ],
        )

    def test_single_async_resetAccessToken(self):
        """TestAsyncAuth | Auth.resetAccessToken single
        """
        self.try_function(
            'resetAccessToken',
            'post',
            argumentNames=['clientId', ],
        )

    def test_multi_async_resetAccessToken(self):
        """TestAsyncAuth | Auth.resetAccessToken multi
        """
        self.try_async_function(
            'resetAccessToken',
            'post',
            argumentNames=['clientId', ],
        )

    def test_single_async_updateClient(self):
        """TestAsyncAuth | Auth.updateClient single
        """
        self.try_function(
            'updateClient',
            'post',
            argumentNames=['clientId', 'payload', ],
        )

    def test_multi_async_updateClient(self):
        """TestAsyncAuth | Auth.updateClient multi
        """
        self.try_async_function(
            'updateClient',
            'post',
            argumentNames=['clientId', 'payload', ],
        )

    def test_single_async_enableClient(self):
        """TestAsyncAuth | Auth.enableClient single
        """
        self.try_function(
            'enableClient',
            'post',
            argumentNames=['clientId', ],
        )

    def test_multi_async_enableClient(self):
        """TestAsyncAuth | Auth.enableClient multi
        """
        self.try_async_function(
            'enableClient',
            'post',
            argumentNames=['clientId', ],
        )

    def test_single_async_disableClient(self):
        """TestAsyncAuth | Auth.disableClient single
        """
        self.try_function(
            'disableClient',
            'post',
            argumentNames=['clientId', ],
        )

    def test_multi_async_disableClient(self):
        """TestAsyncAuth | Auth.disableClient multi
        """
        self.try_async_function(
            'disableClient',
            'post',
            argumentNames=['clientId', ],
        )

    def test_single_async_deleteClient(self):
        """TestAsyncAuth | Auth.deleteClient single
        """
        self.try_function(
            'deleteClient',
            'delete',
            argumentNames=['clientId', ],
        )

    def test_multi_async_deleteClient(self):
        """TestAsyncAuth | Auth.deleteClient multi
        """
        self.try_async_function(
            'deleteClient',
            'delete',
            argumentNames=['clientId', ],
        )

    def test_single_async_listRoles(self):
        """TestAsyncAuth | Auth.listRoles single
        """
        self.try_function(
            'listRoles',
            'get',
            argumentNames=[],
        )

    def test_multi_async_listRoles(self):
        """TestAsyncAuth | Auth.listRoles multi
        """
        self.try_async_function(
            'listRoles',
            'get',
            argumentNames=[],
        )

    def test_single_async_role(self):
        """TestAsyncAuth | Auth.role single
        """
        self.try_function(
            'role',
            'get',
            argumentNames=['roleId', ],
        )

    def test_multi_async_role(self):
        """TestAsyncAuth | Auth.role multi
        """
        self.try_async_function(
            'role',
            'get',
            argumentNames=['roleId', ],
        )

    def test_single_async_createRole(self):
        """TestAsyncAuth | Auth.createRole single
        """
        self.try_function(
            'createRole',
            'put',
            argumentNames=['roleId', 'payload', ],
        )

    def test_multi_async_createRole(self):
        """TestAsyncAuth | Auth.createRole multi
        """
        self.try_async_function(
            'createRole',
            'put',
            argumentNames=['roleId', 'payload', ],
        )

    def test_single_async_updateRole(self):
        """TestAsyncAuth | Auth.updateRole single
        """
        self.try_function(
            'updateRole',
            'post',
            argumentNames=['roleId', 'payload', ],
        )

    def test_multi_async_updateRole(self):
        """TestAsyncAuth | Auth.updateRole multi
        """
        self.try_async_function(
            'updateRole',
            'post',
            argumentNames=['roleId', 'payload', ],
        )

    def test_single_async_deleteRole(self):
        """TestAsyncAuth | Auth.deleteRole single
        """
        self.try_function(
            'deleteRole',
            'delete',
            argumentNames=['roleId', ],
        )

    def test_multi_async_deleteRole(self):
        """TestAsyncAuth | Auth.deleteRole multi
        """
        self.try_async_function(
            'deleteRole',
            'delete',
            argumentNames=['roleId', ],
        )

    def test_single_async_expandScopes(self):
        """TestAsyncAuth | Auth.expandScopes single
        """
        self.try_function(
            'expandScopes',
            'get',
            argumentNames=['payload', ],
        )

    def test_multi_async_expandScopes(self):
        """TestAsyncAuth | Auth.expandScopes multi
        """
        self.try_async_function(
            'expandScopes',
            'get',
            argumentNames=['payload', ],
        )

    def test_single_async_currentScopes(self):
        """TestAsyncAuth | Auth.currentScopes single
        """
        self.try_function(
            'currentScopes',
            'get',
            argumentNames=[],
        )

    def test_multi_async_currentScopes(self):
        """TestAsyncAuth | Auth.currentScopes multi
        """
        self.try_async_function(
            'currentScopes',
            'get',
            argumentNames=[],
        )

    def test_single_async_awsS3Credentials(self):
        """TestAsyncAuth | Auth.awsS3Credentials single
        """
        self.try_function(
            'awsS3Credentials',
            'get',
            argumentNames=['level', 'bucket', 'prefix', ],
        )

    def test_multi_async_awsS3Credentials(self):
        """TestAsyncAuth | Auth.awsS3Credentials multi
        """
        self.try_async_function(
            'awsS3Credentials',
            'get',
            argumentNames=['level', 'bucket', 'prefix', ],
        )

    def test_single_async_azureTableSAS(self):
        """TestAsyncAuth | Auth.azureTableSAS single
        """
        self.try_function(
            'azureTableSAS',
            'get',
            argumentNames=['account', 'table', ],
        )

    def test_multi_async_azureTableSAS(self):
        """TestAsyncAuth | Auth.azureTableSAS multi
        """
        self.try_async_function(
            'azureTableSAS',
            'get',
            argumentNames=['account', 'table', ],
        )

    def test_single_async_sentryDSN(self):
        """TestAsyncAuth | Auth.sentryDSN single
        """
        self.try_function(
            'sentryDSN',
            'get',
            argumentNames=['project', ],
        )

    def test_multi_async_sentryDSN(self):
        """TestAsyncAuth | Auth.sentryDSN multi
        """
        self.try_async_function(
            'sentryDSN',
            'get',
            argumentNames=['project', ],
        )

    def test_single_async_statsumToken(self):
        """TestAsyncAuth | Auth.statsumToken single
        """
        self.try_function(
            'statsumToken',
            'get',
            argumentNames=['project', ],
        )

    def test_multi_async_statsumToken(self):
        """TestAsyncAuth | Auth.statsumToken multi
        """
        self.try_async_function(
            'statsumToken',
            'get',
            argumentNames=['project', ],
        )

    def test_single_async_authenticateHawk(self):
        """TestAsyncAuth | Auth.authenticateHawk single
        """
        self.try_function(
            'authenticateHawk',
            'post',
            argumentNames=['payload', ],
        )

    def test_multi_async_authenticateHawk(self):
        """TestAsyncAuth | Auth.authenticateHawk multi
        """
        self.try_async_function(
            'authenticateHawk',
            'post',
            argumentNames=['payload', ],
        )

    def test_single_async_testAuthenticate(self):
        """TestAsyncAuth | Auth.testAuthenticate single
        """
        self.try_function(
            'testAuthenticate',
            'post',
            argumentNames=['payload', ],
        )

    def test_multi_async_testAuthenticate(self):
        """TestAsyncAuth | Auth.testAuthenticate multi
        """
        self.try_async_function(
            'testAuthenticate',
            'post',
            argumentNames=['payload', ],
        )

    def test_single_async_testAuthenticateGet(self):
        """TestAsyncAuth | Auth.testAuthenticateGet single
        """
        self.try_function(
            'testAuthenticateGet',
            'get',
            argumentNames=[],
        )

    def test_multi_async_testAuthenticateGet(self):
        """TestAsyncAuth | Auth.testAuthenticateGet multi
        """
        self.try_async_function(
            'testAuthenticateGet',
            'get',
            argumentNames=[],
        )

    def test_single_async_ping(self):
        """TestAsyncAuth | Auth.ping single
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
        )

    def test_multi_async_ping(self):
        """TestAsyncAuth | Auth.ping multi
        """
        self.try_async_function(
            'ping',
            'get',
            argumentNames=[],
        )
