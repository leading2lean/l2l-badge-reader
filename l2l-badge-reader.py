#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" L2L Badge Reader Example Application for operator check in (clock in) to a 
production line. This application uses a scanner (keyboard wedge) to read the 
user's badge with the value stored as the user's externalID in L2L. 
For best results, configure your scanner/reader to append an Enter(Return) after the scan.
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
    print(f"L2L Badge-Reader version {__version__}")
    print(f"Check in users for the {CONFIG['linecode']} line at site number {CONFIG['site']}.")

    try:
        # Main loop to look for RFID scans and check users into the line
        while(True):
            scan_value = getpass(f"Scan RFID card to check into the {CONFIG['linecode']} line. (Ctrl-C to Quit)")
            
            # OPTIONAL TODO: Verfiy the scanned badge value and/or look up the user's L2L Username or ExternalID
            # - Use the scan_value above to look up the users name/external ID in your local HR database
            # - Use the looked up value to call the appropriate L2L API
            #   - result = L2L.clockInUser(username, CONFIG['site'], CONFIG['linecode'])
            #   - result = L2L.clockInUserByExternalID(externalID, CONFIG['site'], CONFIG['linecode'])
            
            result = L2L.clockInUserByExternalID(scan_value, CONFIG['site'], CONFIG['linecode'])
            if result['success']:
                print("--- User Successfully Checked In")
            else:
                print(f"--- There was a problem checking in. Please try again or check your configuration settings. (Error: {result['error']})")
    except KeyboardInterrupt:
        pass

# run from command line
if os.getenv('ENVIRONMENT') is None and __name__ == '__main__':
    main()