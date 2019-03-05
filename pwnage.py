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
from sys import argv
import hashlib
import io



# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------
debug = False # extra verbose output



# -----------------------------------------------------------------------------
# Hash input password
# -----------------------------------------------------------------------------
def hash_it(input_password):
    return hashlib.sha1(input_password.encode()).hexdigest()



# -----------------------------------------------------------------------------
# Call the API
# -----------------------------------------------------------------------------
def call_hibp_api(hash_prefix):
    url = 'https://api.pwnedpasswords.com/range/' + hash_prefix
    headers = {
        'api-version': '2',
        'User-Agent': 'Pwnage.py'
    }

    # make the request
    r = requests.get(url, headers=headers)

    # check response code
    if not r.status_code == 200:
        print('Error reaching API')
        if debug:
            print('Response code: ' + str(status_code))
        exit()
    else:
        # return the response text on successful connection
        return r.text



# -----------------------------------------------------------------------------
# Parse response
# -----------------------------------------------------------------------------
def parse_response(hash_suffix, response_text):
    buf = io.StringIO(response_text) # build text parser
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
# Print help
# -----------------------------------------------------------------------------
def print_help():
    print('pwnage.py')
    print('https://github.com/zloether/Pwnage.py')
    print('This script checks passwords against the Have I Been Pwned database')
    print('https://haveibeenpwned.com/')
    print('Usage: Run the script with a password as an argument')
    print('Example: python pwnage.py "thisismypassword"')



# -----------------------------------------------------------------------------
# Bring it all together
# -----------------------------------------------------------------------------
def pwnage(input_password):
    hashed_pass = hash_it(input_password) # get hash of password
    hash_prefix = hashed_pass[:5] # get first 5 characters of hashed password
    hash_suffix = hashed_pass[5:] # get characters except first 5 from hashed password
    if debug:
        print("Input password: " + str(input_password))
        print("Hashed passwword: " + str(hashed_pass))
        print("Hashed password prefix: " + str(hash_prefix))
        print("Hashed password suffix: " + str(hash_suffix))
    
    # call the API
    response_text = call_hibp_api(hash_prefix)

    # parse the API response
    parsed_result = parse_response(hash_suffix, response_text)
    
    if parsed_result:
        print('This password has been pwned ' + str(parsed_result) + ' times!')
    else:
        print('This password has not been pwned yet.')
    
    

# -----------------------------------------------------------------------------
# Run interactively
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    if len(argv) > 1:
       input_password = argv[1]
       pwnage(input_password)
    else:
        print_help()
