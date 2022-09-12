#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" L2L API SDK for operator check in (clock in) to a production line."""

import requests, datetime, json, urllib.parse

__author__ = "Tyler Whitaker"
__copyright__ = "Copyright 2022, L2L Inc"
__credits__ = ["Tyler Whitaker"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Tyler Whitaker"
__email__ = "tyler@L2L.com"
__status__ = "Dev"

DATE_STRING_FORMAT = "%Y-%m-%d"
DATETIME_STRING_FORMAT = "%Y-%m-%d %H:%M:%S"

def getCurrentDateTimeStr(format=DATETIME_STRING_FORMAT):
    """ Returns the current date time in the specified format """
    now = datetime.datetime.now()
    return str(now.strftime(format))

def getCurrentDateStr():
    """ Returns the current date in the default date format """
    return getCurrentDateTimeStr(format=DATE_STRING_FORMAT)


class L2LAPI:
    """ L2L API Class used for calling L2L Dispatch APIs. """
    # Usage examples:
    #    L2L = l2l_api.L2LAPI(CONFIG['server'], CONFIG['apikey'], CONFIG['verbose'], Log_filename)
    #    result = L2L.clockInUserByExternalID(externalID, CONFIG['site'], CONFIG['linecode'])

    def __init__(self, server, auth, verbose = False, log_filename = None):
        self.SERVER = server
        self.AUTH = auth
        self.VERBOSE = verbose
        self.LOGFILENAME = log_filename

    def makeGetRequest(self, api, parameters=None):
        """ Make an API GET call to the Leading2Lean API """
        if parameters is None:
            parameters = {}
        response = requests.get(f"{self.SERVER}{api}?auth={self.AUTH}", params=parameters)
        response_obj = json.loads(response.content)
        self.log(f'{response.status_code}: {response.url}')
        if not response_obj['success']:
            self.log(f"Parameters: {parameters}")
            self.log(f"Response: {response.text}")
        return response_obj

    def makePostRequest(self, api, parameters=None):
        """ Make an API POST call to the Leading2Lean API """
        if parameters is None:
            parameters = {}
        parameters['auth'] = self.AUTH
        response = requests.post(f"{self.SERVER}{api}?auth={self.AUTH}", data=parameters)
        response_obj = json.loads(response.content)
        self.log(f'{response.status_code}: {response.url}')
        if not response_obj['success']:
            self.log(f"Parameters: {parameters}")
            self.log(f"Response: {response.text}")
        return response_obj

    def clockInUser(self, username, site, linecode):
        """ L2L API Users Method: Clock In """
        parameters = {
            'site': site,
            'linecode': linecode,
        }
        username = urllib.parse.quote_plus(username)
        return self.makePostRequest(f"/api/1.0/users/clock_in/{username}/", parameters)

    def clockInUserByExternalID(self, externalid, site, linecode):
        """ L2L API Users Method: Clock In by ExternalID """
        parameters = {
            'site': site,
            'linecode': linecode,
        }
        externalid = urllib.parse.quote_plus(externalid)
        return self.makePostRequest(f"/api/1.0/users/clock_in_by_externalid/{externalid}/", parameters)

    def setUserExternalID(self, username, externalid):
        """ L2L API Users Method: Set a user's ExternalID """
        parameters = {
            'externalid': externalid,
        }
        return self.makePostRequest(f"/api/1.0/users/set_externalid/{username}/", parameters)

    def log(self, str):
        """ Log information to the screen and the log file """
        current_datetime = getCurrentDateTimeStr()
        # strip out API key
        str = str.replace(self.AUTH, "<APIKEY>")
        if self.VERBOSE:
            if type(str) is json:
                print(f"{current_datetime} " + json.dumps(str, indent=4, separators=(',', ': ')))
            else:
                print(f"{current_datetime} {str}")

        if self.LOGFILENAME:
            with open(self.LOGFILENAME, 'a') as l:
                l.write(f"{current_datetime} {str}\n")
        return None

