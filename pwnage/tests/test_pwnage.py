import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import pwnage
from argparse import ArgumentParser
from unittest import mock

def test_parse_arguments(capsys):
    args, parser = pwnage.parse_arguments()
    assert isinstance(parser, ArgumentParser)



def test_password_pwnage(capsys):
    # set test password
    test_password = 'password123'

    # testing method
    result = pwnage.password_pwnage(test_password, print_output=True, return_output=True)

    # capture stdout
    captured = capsys.readouterr()

    # check contents
    assert captured.out.startswith('This password has ')
    assert result == True



def test_account_pwnage(capsys):
    # set test account
    test_account = 'ChunkyLover53@aol.com'

    # testing method
    pwnage.account_pwnage(test_account)

    # capture stdout
    captured = capsys.readouterr()

    # check contents
    assert captured.out.startswith(test_account + ' has been pwned in these breaches:')



def test_generate_password(capsys):
    # test returning output
    password = pwnage.generate_password(print_output=False, return_output=True)

    # check length of returned password
    assert len(password) == 32

    # test printing output
    pwnage.generate_password()

    # capture stdout
    captured = capsys.readouterr()

    # check output
    assert len(captured.out.strip()) == 32

    
    