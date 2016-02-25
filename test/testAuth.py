#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import Auth


class FakeAuth(FakeGenerated, Auth):
    pass


class TestAuth(GeneratedTC):
    """Test the generated TestAuth class.
    """
    testClass = FakeAuth

    def test_urls(self):
        """TestAuth | all urls match the json baseUrls
        """
        self.url_check('Auth')

    def test_routingKeys(self):
        """TestAuth | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('Auth')

    def test_listClients_unsigned(self):
        """TestAuth | Auth.listClients unsigned
        """
        self.try_function(
            'listClients',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_listClients_signed(self):
        """TestAuth | Auth.listClients signed
        """
        self.try_function(
            'listClients',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_client_unsigned(self):
        """TestAuth | Auth.client unsigned
        """
        self.try_function(
            'client',
            'get',
            argumentNames=['clientId', ],
            signUrl=False
        )

    def test_client_signed(self):
        """TestAuth | Auth.client signed
        """
        self.try_function(
            'client',
            'get',
            argumentNames=['clientId', ],
            signUrl=True
        )

    def test_createClient_unsigned(self):
        """TestAuth | Auth.createClient unsigned
        """
        self.try_function(
            'createClient',
            'put',
            argumentNames=['clientId', 'payload', ],
            signUrl=False
        )

    def test_resetAccessToken_unsigned(self):
        """TestAuth | Auth.resetAccessToken unsigned
        """
        self.try_function(
            'resetAccessToken',
            'post',
            argumentNames=['clientId', ],
            signUrl=False
        )

    def test_updateClient_unsigned(self):
        """TestAuth | Auth.updateClient unsigned
        """
        self.try_function(
            'updateClient',
            'post',
            argumentNames=['clientId', 'payload', ],
            signUrl=False
        )

    def test_enableClient_unsigned(self):
        """TestAuth | Auth.enableClient unsigned
        """
        self.try_function(
            'enableClient',
            'post',
            argumentNames=['clientId', ],
            signUrl=False
        )

    def test_disableClient_unsigned(self):
        """TestAuth | Auth.disableClient unsigned
        """
        self.try_function(
            'disableClient',
            'post',
            argumentNames=['clientId', ],
            signUrl=False
        )

    def test_deleteClient_unsigned(self):
        """TestAuth | Auth.deleteClient unsigned
        """
        self.try_function(
            'deleteClient',
            'delete',
            argumentNames=['clientId', ],
            signUrl=False
        )

    def test_listRoles_unsigned(self):
        """TestAuth | Auth.listRoles unsigned
        """
        self.try_function(
            'listRoles',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_listRoles_signed(self):
        """TestAuth | Auth.listRoles signed
        """
        self.try_function(
            'listRoles',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_role_unsigned(self):
        """TestAuth | Auth.role unsigned
        """
        self.try_function(
            'role',
            'get',
            argumentNames=['roleId', ],
            signUrl=False
        )

    def test_role_signed(self):
        """TestAuth | Auth.role signed
        """
        self.try_function(
            'role',
            'get',
            argumentNames=['roleId', ],
            signUrl=True
        )

    def test_createRole_unsigned(self):
        """TestAuth | Auth.createRole unsigned
        """
        self.try_function(
            'createRole',
            'put',
            argumentNames=['roleId', 'payload', ],
            signUrl=False
        )

    def test_updateRole_unsigned(self):
        """TestAuth | Auth.updateRole unsigned
        """
        self.try_function(
            'updateRole',
            'post',
            argumentNames=['roleId', 'payload', ],
            signUrl=False
        )

    def test_deleteRole_unsigned(self):
        """TestAuth | Auth.deleteRole unsigned
        """
        self.try_function(
            'deleteRole',
            'delete',
            argumentNames=['roleId', ],
            signUrl=False
        )

    def test_expandScopes_unsigned(self):
        """TestAuth | Auth.expandScopes unsigned
        """
        self.try_function(
            'expandScopes',
            'get',
            argumentNames=['payload', ],
            signUrl=False
        )

    def test_expandScopes_signed(self):
        """TestAuth | Auth.expandScopes signed
        """
        self.try_function(
            'expandScopes',
            'get',
            argumentNames=['payload', ],
            signUrl=True
        )

    def test_currentScopes_unsigned(self):
        """TestAuth | Auth.currentScopes unsigned
        """
        self.try_function(
            'currentScopes',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_currentScopes_signed(self):
        """TestAuth | Auth.currentScopes signed
        """
        self.try_function(
            'currentScopes',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_awsS3Credentials_unsigned(self):
        """TestAuth | Auth.awsS3Credentials unsigned
        """
        self.try_function(
            'awsS3Credentials',
            'get',
            argumentNames=['level', 'bucket', 'prefix', ],
            signUrl=False
        )

    def test_awsS3Credentials_signed(self):
        """TestAuth | Auth.awsS3Credentials signed
        """
        self.try_function(
            'awsS3Credentials',
            'get',
            argumentNames=['level', 'bucket', 'prefix', ],
            signUrl=True
        )

    def test_azureTableSAS_unsigned(self):
        """TestAuth | Auth.azureTableSAS unsigned
        """
        self.try_function(
            'azureTableSAS',
            'get',
            argumentNames=['account', 'table', ],
            signUrl=False
        )

    def test_azureTableSAS_signed(self):
        """TestAuth | Auth.azureTableSAS signed
        """
        self.try_function(
            'azureTableSAS',
            'get',
            argumentNames=['account', 'table', ],
            signUrl=True
        )

    def test_authenticateHawk_unsigned(self):
        """TestAuth | Auth.authenticateHawk unsigned
        """
        self.try_function(
            'authenticateHawk',
            'post',
            argumentNames=['payload', ],
            signUrl=False
        )

    def test_testAuthenticate_unsigned(self):
        """TestAuth | Auth.testAuthenticate unsigned
        """
        self.try_function(
            'testAuthenticate',
            'post',
            argumentNames=['payload', ],
            signUrl=False
        )

    def test_testAuthenticateGet_unsigned(self):
        """TestAuth | Auth.testAuthenticateGet unsigned
        """
        self.try_function(
            'testAuthenticateGet',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_testAuthenticateGet_signed(self):
        """TestAuth | Auth.testAuthenticateGet signed
        """
        self.try_function(
            'testAuthenticateGet',
            'get',
            argumentNames=[],
            signUrl=True
        )

    def test_ping_unsigned(self):
        """TestAuth | Auth.ping unsigned
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=False
        )

    def test_ping_signed(self):
        """TestAuth | Auth.ping signed
        """
        self.try_function(
            'ping',
            'get',
            argumentNames=[],
            signUrl=True
        )
