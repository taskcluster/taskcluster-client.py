from __future__ import absolute_import, division, print_function

import unittest

import taskcluster.baseclient as bc
import taskcluster.exceptions as exc


FAKE_URL = "https://example.com"


class BC(bc.BaseClient):
    classOptions = {'baseUrl': FAKE_URL}


class TestBaseClient(unittest.TestCase):
    """Test BaseClient
    """
    maxDiff = None

    def test_makeQueryString_no_options(self):
        """test_baseclient | test makeQueryString, no options
        """
        client = BC()
        self.assertEqual(client.makeQueryString(None), '')

    def test_makeQueryString_no_validOptions(self):
        """test_baseclient | test makeQueryString, no validOptions
        """
        client = BC()
        self.assertEqual(client.makeQueryString({'a': 1}), 'a=1')

    def test_makeQueryString_valid_options(self):
        """test_baseclient | test makeQueryString, valid options
        """
        client = BC()
        queryString = client.makeQueryString({'a': '1', 'b': 2}, ['a', 'b', 'c'])
        validStrings = ['a=1&b=2', 'b=2&a=1']
        self.assertTrue(queryString in validStrings)

    def test_makeQueryString_invalid_options(self):
        """test_baseclient | test makeQueryString, invalid options
        """
        client = BC()
        with self.assertRaises(exc.TaskclusterFailure):
            client.makeQueryString({'a': '1', 'b': 2}, ['b'])

    def test_makeFullUrl(self):
        """test_baseclient | test makeFullUrl
        """
        client = BC()
        route = "/asdf/foo/bar"
        url = client.makeFullUrl(route, validOptions=['a', 'b'], options={'a': 1})
        self.assertEqual(url, FAKE_URL + route + "?a=1")
