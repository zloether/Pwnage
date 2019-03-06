#!/usr/bin/env python

#########################################################################################
# NAME: pwnage.py
# 
# Website: https://github.com/zloether/Pwnage.py
#
# Description: Checks passwords against the Have I Been Pwned database to see if 
#               the password has been compromised.
# https://haveibeenpwned.com/
#########################################################################################


# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import requests
import hashlib
import io
import argparse
import urllib



# -----------------------------------------------------------------------------
# Hash input password
# -----------------------------------------------------------------------------
def hash_it(input_password):
    return hashlib.sha1(input_password.encode()).hexdigest()



# -----------------------------------------------------------------------------
# Call the API
# -----------------------------------------------------------------------------
def call_hibp_api(url, debug=False, params=None):
    headers = {
        'api-version': '2',
        'User-Agent': 'pwnage.py'
    }

    if debug:
        print('URL: ' + str(url))
        print('Headers: ' + str(headers))
        print('Params: ' + str(params))
        print('Attempting to connect to API')

    # make the request
    r = requests.get(url, headers=headers, params=params)

    # return response
    return r



# -----------------------------------------------------------------------------
# Look for pwned accounts
# -----------------------------------------------------------------------------
def account_pwnage(input_account, debug=False, truncate_reponse=True):
    # url encode the account
    url_account = urllib.parse.quote(input_account)

    # set parameters for API call
    if truncate_reponse:
        params = {'truncateResponse': 'true', 'includeUnverified': 'true'}
    else:
        #params = None
        params = {'includeUnverified': 'true'}

    # build URL
    url = 'https://haveibeenpwned.com/api/v2/breachedaccount/' + url_account

    # call the API
    response = call_hibp_api(url, debug=debug, params=params)
    
    # parse reponse
    parse_account_response(response, input_account, debug)



# -----------------------------------------------------------------------------
# Parse account response
# -----------------------------------------------------------------------------
def parse_account_response(response, input_account, debug=False):
    if response.status_code == 404: # account not pwned!
        print(str(input_account) + ' has not been pwned!')

    elif response.status_code == 200: # account pwned!
        j = response.json() # get the json
        
        # let's see the bad news
        print(str(input_account + ' has been pwned in these breaches:'))
        
        # loop through json
        for i in j:
            print(i['Name'])

    else:
        print('Error reaching API')
        if debug:
            print('Response code: ' + str(response.status_code))
        exit()



# -----------------------------------------------------------------------------
# Look for pwned passwords
# -----------------------------------------------------------------------------
def password_pwnage(input_password, debug=False):
    hashed_pass = hash_it(input_password) # get hash of password
    hash_prefix = hashed_pass[:5] # get first 5 characters of hashed password
    hash_suffix = hashed_pass[5:] # get characters except first 5 from hashed password
    if debug:
        print("Input password: " + str(input_password))
        print("Hashed passwword: " + str(hashed_pass))
        print("Hashed password prefix: " + str(hash_prefix))
        print("Hashed password suffix: " + str(hash_suffix))
    
    # build URL
    url = 'https://api.pwnedpasswords.com/range/' + hash_prefix

    # call the API
    response = call_hibp_api(url, debug)

    # parse the API response
    parsed_result = parse_password_response(hash_suffix, response, debug)
    
    if parsed_result:
        print('This password has been pwned ' + str(parsed_result) + ' times!')
    else:
        print('This password has not been pwned yet.')



# -----------------------------------------------------------------------------
# Parse password response
# -----------------------------------------------------------------------------
def parse_password_response(hash_suffix, response, debug=False):
    # check response code
    if not response.status_code == 200:
        print('Error reaching API')
        if debug:
            print('Response code: ' + str(response.status_code))
        exit()
    else:
        if debug:
            print('Response code: ' + str(response.status_code))

    buf = io.StringIO(response.text) # build text parser
    line = buf.readline().strip() # get first line of response
    
    # iterate thruogh response text
    while line:
        # split line at colon
        line_suffix, count = line.split(':', 1)
        
        # if the input hash suffix matches the hash suffix for this line
        if hash_suffix.upper() == line_suffix.upper():
            # returns the count
            return count

        # get next line
        line = buf.readline().strip()
    # returns False if the suffix does not match    
    return False



# -----------------------------------------------------------------------------
# Configure argument parser
# -----------------------------------------------------------------------------
def parse_arguments():
    # create parser object
    parser = argparse.ArgumentParser(description='Checks passwords against the ' + \
                                    'Have I Been Pwned database\n' + \
                                    'https://haveibeenpwned.com')

    # setup arugment for handling accounts
    parser.add_argument('-a', '--account', dest='account', metavar='<account>',
                        action='store', help='account to check against database')

    # setup argument for handling passwords
    parser.add_argument('-p', '--password', dest='password', metavar='<password>',
                        action='store', help='password to check against database')

    # setup argument for debug output
    parser.add_argument('-v', '--verbose', action='store_true', dest='debug',
                        help='verbose output, useful for debugging issues')
    
    # parse the arguments
    args = parser.parse_args()
    
    return args, parser



# -----------------------------------------------------------------------------
# Run interactively
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    args, parser = parse_arguments()
    
    if args.password:
        password_pwnage(args.password, debug=args.debug)

    if args.account:
        #account_pwnage(args.account, debug=args.debug, truncate_reponse=False)
        account_pwnage(args.account, debug=args.debug)
    
    if not args.account and not args.password:
        parser.print_help()
