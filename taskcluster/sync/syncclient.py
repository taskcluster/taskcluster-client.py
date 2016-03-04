"""This module is used to interact with taskcluster rest apis"""

from __future__ import absolute_import, division, print_function

import logging
import requests
import time

import taskcluster.exceptions as exceptions
import taskcluster.utils as utils
import taskcluster.baseclient as baseclient

log = logging.getLogger(__name__)


def createSession(*args, **kwargs):
    """ Create a new requests session.  This passes through all positional and
    keyword arguments to the requests.Session() constructor
    """
    return requests.Session(*args, **kwargs)


class SyncClient(baseclient.BaseClient):
    """ Base Class for synchronous API Client Classes (py27). Each individual
    Client class needs to set up its own methods for REST endpoints and Topic
    Exchange routing key patterns.
    """

    def createSession(self, session=None, args=(), kwargs=None):
        if session:
            self.session = session
        else:
            kwargs = kwargs or {}
            self.session = self.session or createSession(*args, **kwargs)
        return self.session

    def makeHttpRequest(self, method, route, payload=None, **kwargs):
        """ Make an HTTP Request for the API endpoint.  This method wraps
        the logic about doing failure retry and passes off the actual work
        of doing an HTTP request to another method."""

        url = self.makeFullUrl(route, **kwargs)
        log.debug('Full URL used is: %s', url)

        hawkExt = self.makeHawkExt()

        # Serialize payload if given
        if payload is not None:
            payload = utils.dumpJson(payload)

        # Do a loop of retries
        retry = -1  # we plus first in the loop, and attempt 1 is retry 0
        retries = self.options['maxRetries']
        while retry < retries:
            retry += 1
            time.sleep(utils.calculateSleepTime(retry))
            headers = self.makeHeaders(method, url, payload, hawkExt)
            log.debug('Making attempt %d', retry)
            try:
                return self._makeHttpRequest(method, url, payload, headers)
            except (exceptions.TaskclusterConnectionError,
                    exceptions.TaskclusterRestFailure) as exc:
                if retry < retries:
                    log.warn("Retrying because of %s" % str(exc))
                    continue
                raise

    def _makeHttpRequest(self, method, url, payload, headers):
        """Synchronous, requests-based
        """
        try:
            response = utils.makeSingleHttpRequest(method, url, payload, headers)
        except requests.exceptions.RequestException as rerr:
            raise exceptions.TaskclusterConnectionError(
                "Failed to establish connection",
                superExc=rerr
            )

        # Handle non 2xx status code and retry if possible
        try:
            response.raise_for_status()
            if response.status_code == 204:
                return None
        except requests.exceptions.RequestException as rerr:
            status = response.status_code
            # Parse messages from errors
            data = None
            try:
                data = response.json()
            except:
                pass  # Ignore JSON errors in error messages
            self._raiseHttpError(status, data, rerr)

        # Try to load JSON
        try:
            return response.json()
        except ValueError:
            return {"response": response}
