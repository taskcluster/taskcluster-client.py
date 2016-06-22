#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
'''
Auth Pulse Exchanges
'''
from __future__ import absolute_import, division, print_function

import logging
from taskcluster.sync.syncclient import SyncClient

log = logging.getLogger(__name__)


class AuthEvents(SyncClient):
    '''
    Auth Pulse Exchanges
    The auth service, typically available at `auth.taskcluster.net`
    is responsible for storing credentials, managing assignment of scopes,
    and validation of request signatures from other services.

    These exchanges provides notifications when credentials or roles are
    updated. This is mostly so that multiple instances of the auth service
    can purge their caches and synchronize state. But you are of course
    welcome to use these for other purposes, monitoring changes for example.
    '''
    version = 0
    referenceUrl = 'http://references.taskcluster.net/auth/v1/exchanges.json'
    routingKeys = {
        'clientCreated': [
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'clientUpdated': [
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'clientDeleted': [
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'roleCreated': [
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'roleUpdated': [
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
        'roleDeleted': [
            {
                'multipleWords': True,
                'name': 'reserved',
                'required': False,
                'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.',
            },
        ],
    }

    def __init__(self, *args, **kwargs):
        self.classOptions = {}
        self.classOptions['exchangePrefix'] = 'exchange/taskcluster-auth/v1/'
        super(AuthEvents, self).__init__(*args, **kwargs)

    def clientCreated(self, routingKeyPattern=None):
        '''
        Client Created Messages

        Message that a new client has been created.

        Generate a routing key pattern for the client-created exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "client-created".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['clientCreated'],
            routingKeyPattern
        )

    def clientUpdated(self, routingKeyPattern=None):
        '''
        Client Updated Messages

        Message that a new client has been updated.

        Generate a routing key pattern for the client-updated exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "client-updated".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['clientUpdated'],
            routingKeyPattern
        )

    def clientDeleted(self, routingKeyPattern=None):
        '''
        Client Deleted Messages

        Message that a new client has been deleted.

        Generate a routing key pattern for the client-deleted exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "client-deleted".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['clientDeleted'],
            routingKeyPattern
        )

    def roleCreated(self, routingKeyPattern=None):
        '''
        Role Created Messages

        Message that a new role has been created.

        Generate a routing key pattern for the role-created exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "role-created".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['roleCreated'],
            routingKeyPattern
        )

    def roleUpdated(self, routingKeyPattern=None):
        '''
        Role Updated Messages

        Message that a new role has been updated.

        Generate a routing key pattern for the role-updated exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "role-updated".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['roleUpdated'],
            routingKeyPattern
        )

    def roleDeleted(self, routingKeyPattern=None):
        '''
        Role Deleted Messages

        Message that a new role has been deleted.

        Generate a routing key pattern for the role-deleted exchange.
        This method takes a given routing key as a string or a dictionary.  For each given
        dictionary key, the corresponding routing key token takes its value.  For routing key
        tokens which are not specified by the dictionary, the * or # character is used depending
        on whether or not the key allows multiple words.

        This exchange takes the following keys:
        - ``reserved``
        '''
        exchangeUrl = '%s/%s' % (self.options['exchangePrefix'].rstrip('/'),
                                 "role-deleted".lstrip('/'))
        return self._makeTopicExchange(
            exchangeUrl,
            self.routingKeys['roleDeleted'],
            routingKeyPattern
        )
