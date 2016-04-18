from __future__ import division, print_function
import unittest
import os

import test.base as base
import taskcluster.client as subject
import taskcluster.runtimeclient as rtclient


@unittest.skipIf(os.environ.get('NO_TESTS_OVER_WIRE'), "Skipping tests over wire")
class TestRuntimeAuthentication(base.BaseAuthentication):

    @property
    def testClass(self):
        return rtclient.createApiClient('Auth', base.APIS_JSON['Auth'])

    def test_no_creds_needed(self):
        self.no_creds_needed()

    def test_permacred_simple(self):
        self.permacred_simple()

    def test_permacred_simple_authorizedScopes(self):
        self.permacred_simple_authorizedScopes()

    def test_unicode_permacred_simple(self):
        self.unicode_permacred_simple()

    def test_invalid_unicode_permacred_simple(self):
        self.invalid_unicode_permacred_simple()

    def test_permacred_insufficient_scopes(self):
        self.permacred_insufficient_scopes()

    def test_temporary_credentials(self):
        self.temporary_credentials()

    def test_named_temporary_credentials(self):
        self.named_temporary_credentials()

    def test_temporary_credentials_authorizedScopes(self):
        self.temporary_credentials_authorizedScopes()

    def test_named_temporary_credentials_authorizedScopes(self):
        self.named_temporary_credentials_authorizedScopes()

    def test_signed_url(self):
        self.signed_url()

    def test_signed_url_bad_credentials(self):
        self.signed_url_bad_credentials()

    def test_temp_credentials_signed_url(self):
        self.temp_credentials_signed_url()

    def test_signed_url_authorizedScopes(self):
        self.signed_url_authorizedScopes()

    def test_temp_credentials_signed_url_authorizedScopes(self):
        self.temp_credentials_signed_url_authorizedScopes()


@unittest.skipIf(os.environ.get('NO_TESTS_OVER_WIRE'), "Skipping tests over wire")
class TestBuildtimeAuthentication(base.BaseAuthentication):

    testClass = subject.Auth

    def test_no_creds_needed(self):
        self.no_creds_needed()

    def test_permacred_simple(self):
        self.permacred_simple()

    def test_permacred_simple_authorizedScopes(self):
        self.permacred_simple_authorizedScopes()

    def test_unicode_permacred_simple(self):
        self.unicode_permacred_simple()

    def test_invalid_unicode_permacred_simple(self):
        self.invalid_unicode_permacred_simple()

    def test_permacred_insufficient_scopes(self):
        self.permacred_insufficient_scopes()

    def test_temporary_credentials(self):
        self.temporary_credentials()

    def test_named_temporary_credentials(self):
        self.named_temporary_credentials()

    def test_temporary_credentials_authorizedScopes(self):
        self.temporary_credentials_authorizedScopes()

    def test_named_temporary_credentials_authorizedScopes(self):
        self.named_temporary_credentials_authorizedScopes()

    def test_signed_url(self):
        self.signed_url()

    def test_signed_url_bad_credentials(self):
        self.signed_url_bad_credentials()

    def test_temp_credentials_signed_url(self):
        self.temp_credentials_signed_url()

    def test_signed_url_authorizedScopes(self):
        self.signed_url_authorizedScopes()

    def test_temp_credentials_signed_url_authorizedScopes(self):
        self.temp_credentials_signed_url_authorizedScopes()
