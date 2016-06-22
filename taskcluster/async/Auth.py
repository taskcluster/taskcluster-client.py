#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Authentication API
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.async.asyncclient import AsyncClient

log = logging.getLogger(__name__)


class Auth(AsyncClient):
    '''
    Authentication API
    Authentication related API end-points for TaskCluster and related
    services. These API end-points are of interest if you wish to:
      * Authenticate request signed with TaskCluster credentials,
      * Manage clients and roles,
      * Inspect or audit clients and roles,
      * Gain access to various services guarded by this API.

    ### Clients
    The authentication service manages _clients_, at a high-level each client
    consists of a `clientId`, an `accessToken`, scopes, and some metadata.
    The `clientId` and `accessToken` can be used for authentication when
    calling TaskCluster APIs.

    The client's scopes control the client's access to TaskCluster resources.
    The scopes are *expanded* by substituting roles, as defined below.

    ### Roles
    A _role_ consists of a `roleId`, a set of scopes and a description.
    Each role constitutes a simple _expansion rule_ that says if you have
    the scope: `assume:<roleId>` you get the set of scopes the role has.
    Think of the `assume:<roleId>` as a scope that allows a client to assume
    a role.

    As in scopes the `*` kleene star also have special meaning if it is
    located at the end of a `roleId`. If you have a role with the following
    `roleId`: `my-prefix*`, then any client which has a scope staring with
    `assume:my-prefix` will be allowed to assume the role.

    ### Guarded Services
    The authentication service also has API end-points for delegating access
    to some guarded service such as AWS S3, or Azure Table Storage.
    Generally, we add API end-points to this server when we wish to use
    TaskCluster credentials to grant access to a third-party service used
    by many TaskCluster components.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/auth/v1/api.json'
    routes = {
        'listClients': '/clients/',
        'client': '/clients/{clientId}',
        'createClient': '/clients/{clientId}',
        'resetAccessToken': '/clients/{clientId}/reset',
        'updateClient': '/clients/{clientId}',
        'enableClient': '/clients/{clientId}/enable',
        'disableClient': '/clients/{clientId}/disable',
        'deleteClient': '/clients/{clientId}',
        'listRoles': '/roles/',
        'role': '/roles/{roleId}',
        'createRole': '/roles/{roleId}',
        'updateRole': '/roles/{roleId}',
        'deleteRole': '/roles/{roleId}',
        'expandScopes': '/scopes/expand',
        'currentScopes': '/scopes/current',
        'awsS3Credentials': '/aws/s3/{level}/{bucket}/{prefix}',
        'azureTableSAS': '/azure/{account}/table/{table}/read-write',
        'sentryDSN': '/sentry/{project}/dsn',
        'statsumToken': '/statsum/{project}/token',
        'authenticateHawk': '/authenticate-hawk',
        'testAuthenticate': '/test-authenticate',
        'testAuthenticateGet': '/test-authenticate-get/',
        'ping': '/ping',
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['baseUrl'] = 'https://auth.taskcluster.net/v1'
        super(Auth, self).__init__(*args, **kwargs)

    async def listClients(self, options=None):
        '''
        List Clients

        Get a list of all clients.  With `prefix`, only clients for which
        it is a prefix of the clientId are returned.

        This method takes no arguments.
        '''
        route = self.makeRoute('listClients')
        validOptions = ['prefix']
        return await self.makeHttpRequest('get', route, options=options, validOptions=validOptions)

    async def client(self, clientId):
        '''
        Get Client

        Get information about a single client.

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('client', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('get', route)

    async def createClient(self, clientId, payload):
        '''
        Create Client

        Create a new client and get the `accessToken` for this client.
        You should store the `accessToken` from this API call as there is no
        other way to retrieve it.

        If you loose the `accessToken` you can call `resetAccessToken` to reset
        it, and a new `accessToken` will be returned, but you cannot retrieve the
        current `accessToken`.

        If a client with the same `clientId` already exists this operation will
        fail. Use `updateClient` if you wish to update an existing client.

        The caller's scopes must satisfy `scopes`.

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('createClient', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('put', route, payload)

    async def resetAccessToken(self, clientId):
        '''
        Reset `accessToken`

        Reset a clients `accessToken`, this will revoke the existing
        `accessToken`, generate a new `accessToken` and return it from this
        call.

        There is no way to retrieve an existing `accessToken`, so if you loose it
        you must reset the accessToken to acquire it again.

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('resetAccessToken', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('post', route)

    async def updateClient(self, clientId, payload):
        '''
        Update Client

        Update an exisiting client. The `clientId` and `accessToken` cannot be
        updated, but `scopes` can be modified.  The caller's scopes must
        satisfy all scopes being added to the client in the update operation.
        If no scopes are given in the request, the client's scopes remain
        unchanged

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('updateClient', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('post', route, payload)

    async def enableClient(self, clientId):
        '''
        Enable Client

        Enable a client that was disabled with `disableClient`.  If the client
        is already enabled, this does nothing.

        This is typically used by identity providers to re-enable clients that
        had been disabled when the corresponding identity's scopes changed.

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('enableClient', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('post', route)

    async def disableClient(self, clientId):
        '''
        Disable Client

        Disable a client.  If the client is already disabled, this does nothing.

        This is typically used by identity providers to disable clients when the
        corresponding identity's scopes no longer satisfy the client's scopes.

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('disableClient', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('post', route)

    async def deleteClient(self, clientId):
        '''
        Delete Client

        Delete a client, please note that any roles related to this client must
        be deleted independently.

        This method takes:
        - ``clientId``
        '''
        route = self.makeRoute('deleteClient', replDict={
            'clientId': clientId,
        })
        return await self.makeHttpRequest('delete', route)

    async def listRoles(self):
        '''
        List Roles

        Get a list of all roles, each role object also includes the list of
        scopes it expands to.

        This method takes no arguments.
        '''
        route = self.makeRoute('listRoles')
        return await self.makeHttpRequest('get', route)

    async def role(self, roleId):
        '''
        Get Role

        Get information about a single role, including the set of scopes that the
        role expands to.

        This method takes:
        - ``roleId``
        '''
        route = self.makeRoute('role', replDict={
            'roleId': roleId,
        })
        return await self.makeHttpRequest('get', route)

    async def createRole(self, roleId, payload):
        '''
        Create Role

        Create a new role.

        The caller's scopes must satisfy the new role's scopes.

        If there already exists a role with the same `roleId` this operation
        will fail. Use `updateRole` to modify an existing role.

        This method takes:
        - ``roleId``
        '''
        route = self.makeRoute('createRole', replDict={
            'roleId': roleId,
        })
        return await self.makeHttpRequest('put', route, payload)

    async def updateRole(self, roleId, payload):
        '''
        Update Role

        Update an existing role.

        The caller's scopes must satisfy all of the new scopes being added, but
        need not satisfy all of the client's existing scopes.

        This method takes:
        - ``roleId``
        '''
        route = self.makeRoute('updateRole', replDict={
            'roleId': roleId,
        })
        return await self.makeHttpRequest('post', route, payload)

    async def deleteRole(self, roleId):
        '''
        Delete Role

        Delete a role. This operation will succeed regardless of whether or not
        the role exists.

        This method takes:
        - ``roleId``
        '''
        route = self.makeRoute('deleteRole', replDict={
            'roleId': roleId,
        })
        return await self.makeHttpRequest('delete', route)

    async def expandScopes(self, payload):
        '''
        Expand Scopes

        Return an expanded copy of the given scopeset, with scopes implied by any
        roles included.

        This method takes no arguments.
        '''
        route = self.makeRoute('expandScopes')
        return await self.makeHttpRequest('get', route, payload)

    async def currentScopes(self):
        '''
        Get Current Scopes

        Return the expanded scopes available in the request, taking into account all sources
        of scopes and scope restrictions (temporary credentials, assumeScopes, client scopes,
        and roles).

        This method takes no arguments.
        '''
        route = self.makeRoute('currentScopes')
        return await self.makeHttpRequest('get', route)

    async def awsS3Credentials(self, level, bucket, prefix):
        '''
        Get Temporary Read/Write Credentials S3

        Get temporary AWS credentials for `read-write` or `read-only` access to
        a given `bucket` and `prefix` within that bucket.
        The `level` parameter can be `read-write` or `read-only` and determines
        which type of credentials are returned. Please note that the `level`
        parameter is required in the scope guarding access.  The bucket name must
        not contain `.`, as recommended by Amazon.

        This method can only allow access to a whitelisted set of buckets.  To add
        a bucket to that whitelist, contact the TaskCluster team, who will add it to
        the appropriate IAM policy.  If the bucket is in a different AWS account, you
        will also need to add a bucket policy allowing access from the TaskCluster
        account.  That policy should look like this:

        ```js
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "allow-taskcluster-auth-to-delegate-access",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::692406183521:root"
              },
              "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject",
                "s3:GetBucketLocation"
              ],
              "Resource": [
                "arn:aws:s3:::<bucket>",
                "arn:aws:s3:::<bucket>/*"
              ]
            }
          ]
        }
        ```

        The credentials are set to expire after an hour, but this behavior is
        subject to change. Hence, you should always read the `expires` property
        from the response, if you intend to maintain active credentials in your
        application.

        Please note that your `prefix` may not start with slash `/`. Such a prefix
        is allowed on S3, but we forbid it here to discourage bad behavior.

        Also note that if your `prefix` doesn't end in a slash `/`, the STS
        credentials may allow access to unexpected keys, as S3 does not treat
        slashes specially.  For example, a prefix of `my-folder` will allow
        access to `my-folder/file.txt` as expected, but also to `my-folder.txt`,
        which may not be intended.

        This method takes:
        - ``level``
        - ``bucket``
        - ``prefix``
        '''
        route = self.makeRoute('awsS3Credentials', replDict={
            'level': level,
            'bucket': bucket,
            'prefix': prefix,
        })
        return await self.makeHttpRequest('get', route)

    async def azureTableSAS(self, account, table):
        '''
        Get Shared-Access-Signature for Azure Table

        Get a shared access signature (SAS) string for use with a specific Azure
        Table Storage table.  Note, this will create the table, if it doesn't
        already exist.

        This method takes:
        - ``account``
        - ``table``
        '''
        route = self.makeRoute('azureTableSAS', replDict={
            'account': account,
            'table': table,
        })
        return await self.makeHttpRequest('get', route)

    async def sentryDSN(self, project):
        '''
        Get DSN for Sentry Project

        Get temporary DSN (access credentials) for a sentry project.
        The credentials returned can be used with any Sentry client for up to
        24 hours, after which the credentials will be automatically disabled.

        If the project doesn't exist it will be created, and assigned to the
        initial team configured for this component. Contact a Sentry admin
        to have the project transferred to a team you have access to if needed

        This method takes:
        - ``project``
        '''
        route = self.makeRoute('sentryDSN', replDict={
            'project': project,
        })
        return await self.makeHttpRequest('get', route)

    async def statsumToken(self, project):
        '''
        Get Token for Statsum Project

        Get temporary `token` and `baseUrl` for sending metrics to statsum.

        The token is valid for 24 hours, clients should refresh after expiration.

        This method takes:
        - ``project``
        '''
        route = self.makeRoute('statsumToken', replDict={
            'project': project,
        })
        return await self.makeHttpRequest('get', route)

    async def authenticateHawk(self, payload):
        '''
        Authenticate Hawk Request

        Validate the request signature given on input and return list of scopes
        that the authenticating client has.

        This method is used by other services that wish rely on TaskCluster
        credentials for authentication. This way we can use Hawk without having
        the secret credentials leave this service.

        This method takes no arguments.
        '''
        route = self.makeRoute('authenticateHawk')
        return await self.makeHttpRequest('post', route, payload)

    async def testAuthenticate(self, payload):
        '''
        Test Authentication

        Utility method to test client implementations of TaskCluster
        authentication.

        Rather than using real credentials, this endpoint accepts requests with
        clientId `tester` and accessToken `no-secret`. That client's scopes are
        based on `clientScopes` in the request body.

        The request is validated, with any certificate, authorizedScopes, etc.
        applied, and the resulting scopes are checked against `requiredScopes`
        from the request body. On success, the response contains the clientId
        and scopes as seen by the API method.

        This method takes no arguments.
        '''
        route = self.makeRoute('testAuthenticate')
        return await self.makeHttpRequest('post', route, payload)

    async def testAuthenticateGet(self):
        '''
        Test Authentication (GET)

        Utility method similar to `testAuthenticate`, but with the GET method,
        so it can be used with signed URLs (bewits).

        Rather than using real credentials, this endpoint accepts requests with
        clientId `tester` and accessToken `no-secret`. That client's scopes are
        `['test:*', 'auth:create-client:test:*']`.  The call fails if the
        `test:authenticate-get` scope is not available.

        The request is validated, with any certificate, authorizedScopes, etc.
        applied, and the resulting scopes are checked, just like any API call.
        On success, the response contains the clientId and scopes as seen by
        the API method.

        This method may later be extended to allow specification of client and
        required scopes via query arguments.

        This method takes no arguments.
        '''
        route = self.makeRoute('testAuthenticateGet')
        return await self.makeHttpRequest('get', route)

    async def ping(self):
        '''
        Ping Server

        Documented later...

        **Warning** this api end-point is **not stable**.

        This method takes no arguments.
        '''
        route = self.makeRoute('ping')
        return await self.makeHttpRequest('get', route)
