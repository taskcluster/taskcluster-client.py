Taskcluster Client Library in Python
======================================

[![Build Status](https://travis-ci.org/taskcluster/taskcluster-client.py.svg?branch=master)](https://travis-ci.org/taskcluster/taskcluster-client.py)

This is a library used to interact with Taskcluster within Python programs.  It
presents the entire REST API to consumers as well as being able to generate
URLs Signed by Hawk credentials.  It can also generate routing keys for
listening to pulse messages from Taskcluster.

The library builds the REST API methods from the same [API Reference
format](http://docs.taskcluster.net/tools/references/index.html) as the
Javascript client library.

## API Documentation

The REST API methods are documented on
[http://docs.taskcluster.net/](http://docs.taskcluster.net/)

## Usage

* Here's a simple command:

    ```python
    import taskcluster
    index = taskcluster.Index({
        'credentials': {
            'clientId': 'id',
            'accessToken': 'accessToken',
            'certificate':  {...}   # Only applicable for temporary credentials
        }
    })
    index.ping()
    ```

* Keyword arguments for API methods are supported.  The javascript client
  accepts only positional arguments.  You may use either positional arguments
  or keyword, never both.  If the method requires an input payload, you must
  specify it as the last positional argument.  If you are using keyword
  arguments, the payload is the first argument.

    ```python
    import taskcluster
    api = taskcluster.api()
    api.method('1', '2', '3', {'data': 'here'})
    ```
    Assuming apiMethod has a route of `/method/<arg1>/<arg2>/<arg3>`,
    this will result in a call to `/method/pie/2/3`

    The same call can be achieved using keyword arguments of:

    ```python
    import taskcluster
    api = taskcluster.api()
    api.method({'data': 'here'}, arg1='1', arg2='2', arg3='3')
    ```

* Options for the topic exchange methods can be in the form of either a single
  dictionary argument or keyword arguments.  Only one form is allowed

    ```python
    from taskcluster import client
    qEvt = client.QueueEvents()
    # The following calls are equivalent
    qEvt.taskCompleted({'taskId': 'atask'})
    qEvt.taskCompleted(taskId='atask')
    ```

* Method Payloads are specified through the `payload` keyword passed to the API
  method.  When using positional arguments, it's the last argument.  When using
  keyword arguments, the payload is the first and only positional argument

    ```python
    from taskcluster import client
    index = client.index()
    index.listNamespaces('mozilla-central', payload={'continuationToken': 'a_token'})
    ```

Logging is set up in `taskcluster/__init__.py`.  If the special `DEBUG_TASKCLUSTER_CLIENT`
environment variable is set, the `__init__.py` module will set the `logging` module's level
for its logger to `logging.DEBUG` and if there are no existing handlers, add a
`logging.StreamHandler()` instance.  This is meant to assist those who do not wish to bother
figuring out how to configure the python logging module but do want debug messages


## Generating Temporary Credentials
If you have non-temporary taskcluster credentials you can generate a set of
temporary credentials as follows. Notice that the credentials cannot last more
than 31 days, and you can only revoke them by revoking the credentials that was
used to issue them (this takes up to one hour).

```python
import datetime

credentials = taskcluster.createTemporaryCredentials(
    # issuing clientId
    clientId,
    # issuing accessToken
    accessToken,
    # Validity of temporary credentials starts here, in timestamp
    start,
    # Expiration of temporary credentials, in timestamp
    expiry,
    # Scopes to grant the temporary credentials
    scopes: ['ScopeA', 'ScopeB', ...],
    # credential name (optional)
    name='...'
)
```

You cannot use temporary credentials to issue new temporary credentials.  You
must have `auth:create-client:<name>` to create a named temporary credential,
but unnamed temporary credentials can be created regardless of your scopes.

## Async support

There is support for async clients, for python 3.5.  To use those client calls, import from `taskcluster.async` instead of from `taskcluster` or `taskcluster.sync`.  These methods need to be `await`ed or run through the event loop.

```python
# Create Auth client instance
from taskcluster.async import Auth
import asyncio
auth = Auth(options)
# The below will essentially make a synchronous call, since we're waiting on a single async method.
loop = asyncio.get_event_loop()
result = loop.run_until_complete(auth.ping())
```

## Scopes

The `scope_match(assumed_scopes, required_scope_sets)` function determines
whether one or more of a set of required scopes are satisfied by the assumed
scopes, taking *-expansion into account.  This is useful for making local
decisions on scope satisfaction, but note that `assumed_scopes` must be the
*expanded* scopes, as this function cannot perform expansion.

It takes a list of a assumed scopes, and a list of required scope sets on
disjunctive normal form, and checks if any of the required scope sets are
satisfied.

Example:

```
    required_scope_sets = [
        ["scopeA", "scopeB"],
        ["scopeC:*"]
    ]
    assert     scopes_match(['scopeA', 'scopeB'], required_scope_sets)
    assert     scopes_match(['scopeC:xyz'], required_scope_sets)
    assert not scopes_match(['scopeA'], required_scope_sets)
    assert not scopes_match(['scopeC'], required_scope_sets)
```

## createApiClient

We no longer need to use `createApiClient`, because all of the APIs defined in the APIS_JSON have code generated at buildtime via `make gencode`.

However, if you want to generate a runtime api client,

```python
# Create a runtime client instance
from taskcluster.runtimeclient import createApiClient
API_DEFN = {
    ...
}
client = createApiClient('Name', API_DEFN)
```

## Methods contained in the client library

<!-- START OF GENERATED DOCS -->

### Methods in `taskcluster.Auth`
```python
// Create Auth client instance
import taskcluster
auth = taskcluster.Auth(options)
```
#### List Clients
 * `auth.listClients() -> result`

#### Get Client
 * `auth.client(clientId) -> result`
 * `auth.client(clientId='value') -> result`

#### Create Client
 * `auth.createClient(clientId, payload) -> result`
 * `auth.createClient(payload, clientId='value') -> result`

#### Reset `accessToken`
 * `auth.resetAccessToken(clientId) -> result`
 * `auth.resetAccessToken(clientId='value') -> result`

#### Update Client
 * `auth.updateClient(clientId, payload) -> result`
 * `auth.updateClient(payload, clientId='value') -> result`

#### Enable Client
 * `auth.enableClient(clientId) -> result`
 * `auth.enableClient(clientId='value') -> result`

#### Disable Client
 * `auth.disableClient(clientId) -> result`
 * `auth.disableClient(clientId='value') -> result`

#### Delete Client
 * `auth.deleteClient(clientId) -> None`
 * `auth.deleteClient(clientId='value') -> None`

#### List Roles
 * `auth.listRoles() -> result`

#### Get Role
 * `auth.role(roleId) -> result`
 * `auth.role(roleId='value') -> result`

#### Create Role
 * `auth.createRole(roleId, payload) -> result`
 * `auth.createRole(payload, roleId='value') -> result`

#### Update Role
 * `auth.updateRole(roleId, payload) -> result`
 * `auth.updateRole(payload, roleId='value') -> result`

#### Delete Role
 * `auth.deleteRole(roleId) -> None`
 * `auth.deleteRole(roleId='value') -> None`

#### Expand Scopes
 * `auth.expandScopes(payload) -> result`

#### Get Current Scopes
 * `auth.currentScopes() -> result`

#### Get Temporary Read/Write Credentials S3
 * `auth.awsS3Credentials(level, bucket, prefix) -> result`
 * `auth.awsS3Credentials(level='value', bucket='value', prefix='value') -> result`

#### Get Shared-Access-Signature for Azure Table
 * `auth.azureTableSAS(account, table) -> result`
 * `auth.azureTableSAS(account='value', table='value') -> result`

#### Get DSN for Sentry Project
 * `auth.sentryDSN(project) -> result`
 * `auth.sentryDSN(project='value') -> result`

#### Get Token for Statsum Project
 * `auth.statsumToken(project) -> result`
 * `auth.statsumToken(project='value') -> result`

#### Authenticate Hawk Request
 * `auth.authenticateHawk(payload) -> result`

#### Test Authentication
 * `auth.testAuthenticate(payload) -> result`

#### Test Authentication (GET)
 * `auth.testAuthenticateGet() -> result`

#### Ping Server
 * `auth.ping() -> None`




### Exchanges in `taskcluster.AuthEvents`
```python
// Create AuthEvents client instance
import taskcluster
authEvents = taskcluster.AuthEvents(options)
```
#### Client Created Messages
 * `authEvents.clientCreated(routingKeyPattern) -> routingKey`
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Client Updated Messages
 * `authEvents.clientUpdated(routingKeyPattern) -> routingKey`
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Client Deleted Messages
 * `authEvents.clientDeleted(routingKeyPattern) -> routingKey`
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Role Created Messages
 * `authEvents.roleCreated(routingKeyPattern) -> routingKey`
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Role Updated Messages
 * `authEvents.roleUpdated(routingKeyPattern) -> routingKey`
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Role Deleted Messages
 * `authEvents.roleDeleted(routingKeyPattern) -> routingKey`
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.




### Methods in `taskcluster.AwsProvisioner`
```python
// Create AwsProvisioner client instance
import taskcluster
awsProvisioner = taskcluster.AwsProvisioner(options)
```
#### List worker types with details
 * `awsProvisioner.listWorkerTypeSummaries() -> result`

#### Create new Worker Type
 * `awsProvisioner.createWorkerType(workerType, payload) -> result`
 * `awsProvisioner.createWorkerType(payload, workerType='value') -> result`

#### Update Worker Type
 * `awsProvisioner.updateWorkerType(workerType, payload) -> result`
 * `awsProvisioner.updateWorkerType(payload, workerType='value') -> result`

#### Get Worker Type
 * `awsProvisioner.workerType(workerType) -> result`
 * `awsProvisioner.workerType(workerType='value') -> result`

#### Delete Worker Type
 * `awsProvisioner.removeWorkerType(workerType) -> None`
 * `awsProvisioner.removeWorkerType(workerType='value') -> None`

#### List Worker Types
 * `awsProvisioner.listWorkerTypes() -> result`

#### Create new Secret
 * `awsProvisioner.createSecret(token, payload) -> None`
 * `awsProvisioner.createSecret(payload, token='value') -> None`

#### Get a Secret
 * `awsProvisioner.getSecret(token) -> result`
 * `awsProvisioner.getSecret(token='value') -> result`

#### Report an instance starting
 * `awsProvisioner.instanceStarted(instanceId, token) -> None`
 * `awsProvisioner.instanceStarted(instanceId='value', token='value') -> None`

#### Remove a Secret
 * `awsProvisioner.removeSecret(token) -> None`
 * `awsProvisioner.removeSecret(token='value') -> None`

#### Get All Launch Specifications for WorkerType
 * `awsProvisioner.getLaunchSpecs(workerType) -> result`
 * `awsProvisioner.getLaunchSpecs(workerType='value') -> result`

#### Get AWS State for a worker type
 * `awsProvisioner.state(workerType) -> None`
 * `awsProvisioner.state(workerType='value') -> None`

#### Ping Server
 * `awsProvisioner.ping() -> None`

#### Backend Status
 * `awsProvisioner.backendStatus() -> result`




### Exchanges in `taskcluster.AwsProvisionerEvents`
```python
// Create AwsProvisionerEvents client instance
import taskcluster
awsProvisionerEvents = taskcluster.AwsProvisionerEvents(options)
```
#### WorkerType Created Message
 * `awsProvisionerEvents.workerTypeCreated(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * workerType is required  Description: WorkerType that this message concerns.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### WorkerType Updated Message
 * `awsProvisionerEvents.workerTypeUpdated(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * workerType is required  Description: WorkerType that this message concerns.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### WorkerType Removed Message
 * `awsProvisionerEvents.workerTypeRemoved(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * workerType is required  Description: WorkerType that this message concerns.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.




### Methods in `taskcluster.Github`
```python
// Create Github client instance
import taskcluster
github = taskcluster.Github(options)
```
#### Consume GitHub WebHook
 * `github.githubWebHookConsumer() -> None`

#### Ping Server
 * `github.ping() -> None`




### Exchanges in `taskcluster.GithubEvents`
```python
// Create GithubEvents client instance
import taskcluster
githubEvents = taskcluster.GithubEvents(options)
```
#### GitHub Pull Request Event
 * `githubEvents.pullRequest(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key.
   * organization is required  Description: The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.
   * repository is required  Description: The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.
   * action is required  Description: The GitHub `action` which triggered an event. See for possible values see the payload actions property.

#### GitHub push Event
 * `githubEvents.push(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `"primary"` for the formalized routing key.
   * organization is required  Description: The GitHub `organization` which had an event. All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.
   * repository is required  Description: The GitHub `repository` which had an event.All periods have been replaced by % - such that foo.bar becomes foo%bar - and all other special characters aside from - and _ have been stripped.




### Methods in `taskcluster.Hooks`
```python
// Create Hooks client instance
import taskcluster
hooks = taskcluster.Hooks(options)
```
#### List hook groups
 * `hooks.listHookGroups() -> result`

#### List hooks in a given group
 * `hooks.listHooks(hookGroupId) -> result`
 * `hooks.listHooks(hookGroupId='value') -> result`

#### Get hook definition
 * `hooks.hook(hookGroupId, hookId) -> result`
 * `hooks.hook(hookGroupId='value', hookId='value') -> result`

#### Get hook status
 * `hooks.getHookStatus(hookGroupId, hookId) -> result`
 * `hooks.getHookStatus(hookGroupId='value', hookId='value') -> result`

#### Get hook schedule
 * `hooks.getHookSchedule(hookGroupId, hookId) -> result`
 * `hooks.getHookSchedule(hookGroupId='value', hookId='value') -> result`

#### Create a hook
 * `hooks.createHook(hookGroupId, hookId, payload) -> result`
 * `hooks.createHook(payload, hookGroupId='value', hookId='value') -> result`

#### Update a hook
 * `hooks.updateHook(hookGroupId, hookId, payload) -> result`
 * `hooks.updateHook(payload, hookGroupId='value', hookId='value') -> result`

#### Delete a hook
 * `hooks.removeHook(hookGroupId, hookId) -> None`
 * `hooks.removeHook(hookGroupId='value', hookId='value') -> None`




### Methods in `taskcluster.Index`
```python
// Create Index client instance
import taskcluster
index = taskcluster.Index(options)
```
#### Find Indexed Task
 * `index.findTask(namespace) -> result`
 * `index.findTask(namespace='value') -> result`

#### List Namespaces
 * `index.listNamespaces(namespace, payload) -> result`
 * `index.listNamespaces(payload, namespace='value') -> result`

#### List Tasks
 * `index.listTasks(namespace, payload) -> result`
 * `index.listTasks(payload, namespace='value') -> result`

#### Insert Task into Index
 * `index.insertTask(namespace, payload) -> result`
 * `index.insertTask(payload, namespace='value') -> result`

#### Get Artifact From Indexed Task
 * `index.findArtifactFromTask(namespace, name) -> None`
 * `index.findArtifactFromTask(namespace='value', name='value') -> None`

#### Ping Server
 * `index.ping() -> None`




### Methods in `taskcluster.Login`
```python
// Create Login client instance
import taskcluster
login = taskcluster.Login(options)
```
#### Get TaskCluster credentials given a Persona assertion
 * `login.credentialsFromPersonaAssertion(payload) -> result`

#### Ping Server
 * `login.ping() -> None`




### Methods in `taskcluster.PurgeCache`
```python
// Create PurgeCache client instance
import taskcluster
purgeCache = taskcluster.PurgeCache(options)
```
#### Purge Worker Cache
 * `purgeCache.purgeCache(provisionerId, workerType, payload) -> None`
 * `purgeCache.purgeCache(payload, provisionerId='value', workerType='value') -> None`

#### Ping Server
 * `purgeCache.ping() -> None`




### Exchanges in `taskcluster.PurgeCacheEvents`
```python
// Create PurgeCacheEvents client instance
import taskcluster
purgeCacheEvents = taskcluster.PurgeCacheEvents(options)
```
#### Purge Cache Messages
 * `purgeCacheEvents.purgeCache(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * provisionerId is required  Description: `provisionerId` under which to purge cache.
   * workerType is required  Description: `workerType` for which to purge cache.




### Methods in `taskcluster.Queue`
```python
// Create Queue client instance
import taskcluster
queue = taskcluster.Queue(options)
```
#### Get Task Definition
 * `queue.task(taskId) -> result`
 * `queue.task(taskId='value') -> result`

#### Get task status
 * `queue.status(taskId) -> result`
 * `queue.status(taskId='value') -> result`

#### List Task Group
 * `queue.listTaskGroup(taskGroupId) -> result`
 * `queue.listTaskGroup(taskGroupId='value') -> result`

#### List Dependent Tasks
 * `queue.listDependentTasks(taskId) -> result`
 * `queue.listDependentTasks(taskId='value') -> result`

#### Create New Task
 * `queue.createTask(taskId, payload) -> result`
 * `queue.createTask(payload, taskId='value') -> result`

#### Define Task
 * `queue.defineTask(taskId, payload) -> result`
 * `queue.defineTask(payload, taskId='value') -> result`

#### Schedule Defined Task
 * `queue.scheduleTask(taskId) -> result`
 * `queue.scheduleTask(taskId='value') -> result`

#### Rerun a Resolved Task
 * `queue.rerunTask(taskId) -> result`
 * `queue.rerunTask(taskId='value') -> result`

#### Cancel Task
 * `queue.cancelTask(taskId) -> result`
 * `queue.cancelTask(taskId='value') -> result`

#### Get Urls to Poll Pending Tasks
 * `queue.pollTaskUrls(provisionerId, workerType) -> result`
 * `queue.pollTaskUrls(provisionerId='value', workerType='value') -> result`

#### Claim task
 * `queue.claimTask(taskId, runId, payload) -> result`
 * `queue.claimTask(payload, taskId='value', runId='value') -> result`

#### Reclaim task
 * `queue.reclaimTask(taskId, runId) -> result`
 * `queue.reclaimTask(taskId='value', runId='value') -> result`

#### Report Run Completed
 * `queue.reportCompleted(taskId, runId) -> result`
 * `queue.reportCompleted(taskId='value', runId='value') -> result`

#### Report Run Failed
 * `queue.reportFailed(taskId, runId) -> result`
 * `queue.reportFailed(taskId='value', runId='value') -> result`

#### Report Task Exception
 * `queue.reportException(taskId, runId, payload) -> result`
 * `queue.reportException(payload, taskId='value', runId='value') -> result`

#### Create Artifact
 * `queue.createArtifact(taskId, runId, name, payload) -> result`
 * `queue.createArtifact(payload, taskId='value', runId='value', name='value') -> result`

#### Get Artifact from Run
 * `queue.getArtifact(taskId, runId, name) -> None`
 * `queue.getArtifact(taskId='value', runId='value', name='value') -> None`

#### Get Artifact from Latest Run
 * `queue.getLatestArtifact(taskId, name) -> None`
 * `queue.getLatestArtifact(taskId='value', name='value') -> None`

#### Get Artifacts from Run
 * `queue.listArtifacts(taskId, runId) -> result`
 * `queue.listArtifacts(taskId='value', runId='value') -> result`

#### Get Artifacts from Latest Run
 * `queue.listLatestArtifacts(taskId) -> result`
 * `queue.listLatestArtifacts(taskId='value') -> result`

#### Get Number of Pending Tasks
 * `queue.pendingTasks(provisionerId, workerType) -> result`
 * `queue.pendingTasks(provisionerId='value', workerType='value') -> result`

#### Ping Server
 * `queue.ping() -> None`




### Exchanges in `taskcluster.QueueEvents`
```python
// Create QueueEvents client instance
import taskcluster
queueEvents = taskcluster.QueueEvents(options)
```
#### Task Defined Messages
 * `queueEvents.taskDefined(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task Pending Messages
 * `queueEvents.taskPending(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId is required  Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task Running Messages
 * `queueEvents.taskRunning(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId is required  Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup is required  Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId is required  Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Artifact Creation Messages
 * `queueEvents.artifactCreated(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId is required  Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup is required  Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId is required  Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task Completed Messages
 * `queueEvents.taskCompleted(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId is required  Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup is required  Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId is required  Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task Failed Messages
 * `queueEvents.taskFailed(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task Exception Messages
 * `queueEvents.taskException(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId is required  Description: `taskId` for the task this message concerns
   * runId Description: `runId` of latest run for the task, `_` if no run is exists for the task.
   * workerGroup Description: `workerGroup` of latest run for the task, `_` if no run is exists for the task.
   * workerId Description: `workerId` of latest run for the task, `_` if no run is exists for the task.
   * provisionerId is required  Description: `provisionerId` this task is targeted at.
   * workerType is required  Description: `workerType` this task must run on.
   * schedulerId is required  Description: `schedulerId` this task was created by.
   * taskGroupId is required  Description: `taskGroupId` this task was created in.
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.




### Methods in `taskcluster.Scheduler`
```python
// Create Scheduler client instance
import taskcluster
scheduler = taskcluster.Scheduler(options)
```
#### Create new task-graph
 * `scheduler.createTaskGraph(taskGraphId, payload) -> result`
 * `scheduler.createTaskGraph(payload, taskGraphId='value') -> result`

#### Extend existing task-graph
 * `scheduler.extendTaskGraph(taskGraphId, payload) -> result`
 * `scheduler.extendTaskGraph(payload, taskGraphId='value') -> result`

#### Task Graph Status
 * `scheduler.status(taskGraphId) -> result`
 * `scheduler.status(taskGraphId='value') -> result`

#### Task Graph Information
 * `scheduler.info(taskGraphId) -> result`
 * `scheduler.info(taskGraphId='value') -> result`

#### Inspect Task Graph
 * `scheduler.inspect(taskGraphId) -> result`
 * `scheduler.inspect(taskGraphId='value') -> result`

#### Inspect Task from a Task-Graph
 * `scheduler.inspectTask(taskGraphId, taskId) -> result`
 * `scheduler.inspectTask(taskGraphId='value', taskId='value') -> result`

#### Ping Server
 * `scheduler.ping() -> None`




### Exchanges in `taskcluster.SchedulerEvents`
```python
// Create SchedulerEvents client instance
import taskcluster
schedulerEvents = taskcluster.SchedulerEvents(options)
```
#### Task-Graph Running Message
 * `schedulerEvents.taskGraphRunning(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId Description: Always takes the value `_`
   * runId Description: Always takes the value `_`
   * workerGroup Description: Always takes the value `_`
   * workerId Description: Always takes the value `_`
   * provisionerId Description: Always takes the value `_`
   * workerType Description: Always takes the value `_`
   * schedulerId is required  Description: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.
   * taskGraphId is required  Description: Identifier for the task-graph this message concerns
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task-Graph Extended Message
 * `schedulerEvents.taskGraphExtended(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId Description: Always takes the value `_`
   * runId Description: Always takes the value `_`
   * workerGroup Description: Always takes the value `_`
   * workerId Description: Always takes the value `_`
   * provisionerId Description: Always takes the value `_`
   * workerType Description: Always takes the value `_`
   * schedulerId is required  Description: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.
   * taskGraphId is required  Description: Identifier for the task-graph this message concerns
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task-Graph Blocked Message
 * `schedulerEvents.taskGraphBlocked(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId Description: Always takes the value `_`
   * runId Description: Always takes the value `_`
   * workerGroup Description: Always takes the value `_`
   * workerId Description: Always takes the value `_`
   * provisionerId Description: Always takes the value `_`
   * workerType Description: Always takes the value `_`
   * schedulerId is required  Description: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.
   * taskGraphId is required  Description: Identifier for the task-graph this message concerns
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.

#### Task-Graph Finished Message
 * `schedulerEvents.taskGraphFinished(routingKeyPattern) -> routingKey`
   * routingKeyKind is constant of `primary`  is required  Description: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.
   * taskId Description: Always takes the value `_`
   * runId Description: Always takes the value `_`
   * workerGroup Description: Always takes the value `_`
   * workerId Description: Always takes the value `_`
   * provisionerId Description: Always takes the value `_`
   * workerType Description: Always takes the value `_`
   * schedulerId is required  Description: Identifier for the task-graphs scheduler managing the task-graph this message concerns. Usually `task-graph-scheduler` in production.
   * taskGraphId is required  Description: Identifier for the task-graph this message concerns
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.




### Methods in `taskcluster.Secrets`
```python
// Create Secrets client instance
import taskcluster
secrets = taskcluster.Secrets(options)
```
#### Set Secret
 * `secrets.set(name, payload) -> None`
 * `secrets.set(payload, name='value') -> None`

#### Delete Secret
 * `secrets.remove(name) -> None`
 * `secrets.remove(name='value') -> None`

#### Read Secret
 * `secrets.get(name) -> result`
 * `secrets.get(name='value') -> result`

#### List Secrets
 * `secrets.list() -> result`

#### Ping Server
 * `secrets.ping() -> None`




### Exchanges in `taskcluster.TreeherderEvents`
```python
// Create TreeherderEvents client instance
import taskcluster
treeherderEvents = taskcluster.TreeherderEvents(options)
```
#### Job Messages
 * `treeherderEvents.jobs(routingKeyPattern) -> routingKey`
   * destination is required  Description: destination
   * project is required  Description: project
   * reserved Description: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.



<!-- END OF GENERATED DOCS -->
