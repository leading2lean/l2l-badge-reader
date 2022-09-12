#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" L2L Setup User Badge Example Application for setting up an users badge for use 
with the l2l-badge reader example application. This application allows the user to
enter a username and scan a badge. It then sets the user's externalID field in L2L 
Dispatch with the badge value for future lookup by the l2l-badge-reader application.

NOTES:
 - Do not use this application is your site uses the user externalid field for 
some other purpose, because it will overwrite the current value and mess up some 
other intergration. 
 - Do not deploy this file to the shop floor. This is only for use by HR/IT employees.
"""

import os, json
from getpass import getpass
import l2l_api

__author__ = "Tyler Whitaker"
__copyright__ = "Copyright 2022, L2L Inc"
__credits__ = ["Tyler Whitaker"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Tyler Whitaker"
__email__ = "tyler@L2L.com"
__status__ = "Dev"


def main():
    # change directory to the location of this file
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # load the config file
    with open('config.json') as config:
        CONFIG = json.load(config)

    # clean up config
    current_path = os.path.dirname(os.path.realpath(__file__))
    log_directory = CONFIG['logdirectory']
    if not log_directory or not os.path.isdir(log_directory):
        log_directory = current_path
    else:
        log_directory = log_directory.rstrip('/')
    LOGFILENAME = log_directory + '/log-' + l2l_api.getCurrentDateStr() + '.log'
    
    L2L = l2l_api.L2LAPI(CONFIG['server'], CONFIG['apikey'], CONFIG['verbose'], LOGFILENAME)

    # Print out Header
    print(f"L2L Setup User Badge Application version {__version__}")
    print(f"Warning: Do not use this application if your company uses the user's externalID field for some other purpose.")
    username = input(f"Enter the user's L2L username: ")
    scan_value = input(f"Scan RFID card: ")
            
    result = L2L.setUserExternalID(username, scan_value)
    if result['success']:
        print(f"--- User Badge Successfully Setup for Username: {username}, Badge Value: {scan_value}")
    else:
        print(f"--- There was a problem setting the users externalID for Username: {username}, Badge Value: {scan_value}")
        print(f"--- Please try again or check your configuration settings. (Error: {result['error']})")


# run from command line
if os.getenv('ENVIRONMENT') is None and __name__ == '__main__':
    main()