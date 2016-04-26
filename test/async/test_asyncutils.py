from __future__ import division, print_function
import aiohttp
import asyncio
import mock

from test.async import getExceptionSession, getFailFirstSession, getFakeSession
from test.base import TCTest
import taskcluster.async.asyncutils as asyncutils
import taskcluster.exceptions as exceptions
import taskcluster.utils as utils


class TestAsyncutils(TCTest):

    def _too_many_exception_retries(self, exception=aiohttp.ClientError,
                                    expectedRetries=utils.MAX_RETRIES + 1):
        """helper method to hit all the try/excepts in asyncutils.makeHttpRequest
        """
        session = getExceptionSession(exception=exception)

        with mock.patch.object(utils, 'calculateSleepTime') as p:
            p.return_value = .001
            with self.assertRaises(exception):
                asyncio.get_event_loop().run_until_complete(
                    asyncutils.makeHttpRequest('get', 'http://example.com',
                                               '{"clientScopes": ["a"]}',
                                               {}, session=session)
                )

        self.assertEqual(expectedRetries, session.count)

    def test_putFile(self):
        """test_asyncutils | putFile
        """
        payload = {'a': 'b'}
        session = getFakeSession(payload=payload)
        result = asyncio.get_event_loop().run_until_complete(
            asyncutils.putFile(__file__, "http://example.com",
                               "text/plain", session=session)
        )
        result_json = yield from result.json()
        self.assertEqual(result_json, payload)

    def test_too_many_retries(self):
        """test_asyncutils | too many retries
        """
        session = getFailFirstSession(firstSuccess=10)

        with mock.patch.object(utils, 'calculateSleepTime') as p:
            p.return_value = .001
            with self.assertRaises(exceptions.TaskclusterRestFailure):
                asyncio.get_event_loop().run_until_complete(
                    asyncutils.makeHttpRequest('get', 'http://example.com',
                                               '{"clientScopes": ["a"]}',
                                               {}, session=session)
                )

    def test_too_many_exception_retries(self):
        """test_asyncutils | too many exception retries
        """
        self._too_many_exception_retries()

    def test_makeHttpRequest_ValueError(self):
        """test_asyncutils | makeHttpRequest ValueError
        """
        self._too_many_exception_retries(exception=ValueError, expectedRetries=1)

    def test_makeHttpRequest_RuntimeError(self):
        """test_asyncutils | makeHttpRequest RuntimeError
        """
        self._too_many_exception_retries(exception=RuntimeError, expectedRetries=1)
