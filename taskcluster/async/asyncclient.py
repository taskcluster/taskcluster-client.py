"""This module is used to interact with taskcluster rest apis"""

from __future__ import absolute_import, division, print_function, unicode_literals

import logging
import asyncio
import aiohttp

from contextlib import contextmanager

import taskcluster.exceptions as exceptions
import taskcluster.baseclient as baseclient
import taskcluster.utils as utils
from taskcluster.async.asyncutils import createSession, makeSingleHttpRequest

log = logging.getLogger(__name__)


class AsyncClient(baseclient.BaseClient):
    """Async class for API Client Classes. Each individual Client class
    needs to set up its own methods for REST endpoints and Topic Exchange
    routing key patterns.
    """

    @contextmanager
    def contextSession(self, *args, **kwargs):
        yield self.createSession(*args, **kwargs)

    def createSession(self, session=None, args=(), kwargs=None):
        if session:
            self.session = session
        else:
            kwargs = kwargs or {}
            self.session = self.session or createSession(*args, **kwargs)
        return self.session

    async def makeHttpRequest(self, method, route, payload=None, session=None, **kwargs):
        """ Make an HTTP Request for the API endpoint.  This method wraps
        the logic about doing failure retry and passes off the actual work
        of doing an HTTP request to another method."""

        url = self.makeFullUrl(route, **kwargs)
        log.debug('Full URL used is: %s', url)

        hawkExt = self.makeHawkExt()

        # Serialize payload if given
        if payload is not None and isinstance(payload, dict):
            payload = utils.dumpJson(payload)

        # Do a loop of retries
        retry = -1  # we plus first in the loop, and attempt 1 is retry 0
        retries = self.options['maxRetries']
        with self.contextSession(session=session) as session:
            while True:
                retry += 1
                await asyncio.sleep(utils.calculateSleepTime(retry))
                headers = self.makeHeaders(method, url, payload, hawkExt)
                log.debug('Making attempt %d', retry)
                try:
                    return await self._makeHttpRequest(method, url, payload,
                                                       headers, session=session)
                except (exceptions.TaskclusterConnectionError,
                        exceptions.TaskclusterRestFailure) as exc:
                    if retry < retries:
                        log.warn("Retrying because of %s" % str(exc))
                        continue
                    raise

    async def _makeHttpRequest(self, method, url, payload, headers, session=None):
        """Asynchronous aiohttp-based
        """
        try:
            response = await makeSingleHttpRequest(
                method, url, payload, headers, session=session
            )
        except aiohttp.ClientError as rerr:
            raise exceptions.TaskclusterConnectionError(
                "Failed to establish connection",
                superExc=rerr
            )

        # Handle non 2xx status code and retry if possible
        status = response.status
        if status == 204:
            return None
        if status != 200:
            # Parse messages from errors
            data = None
            try:
                data = await response.json()
            except:
                pass  # Ignore JSON errors in error messages
            self._raiseHttpError(status, data, None)

        # Try to load JSON
        try:
            return await response.json()
        except ValueError:
            return {"response": response}
