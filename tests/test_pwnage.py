import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import pwnage
from argparse import ArgumentParser

def test_parse_arguments(capsys):
    args, parser = pwnage.parse_arguments()
    assert isinstance(parser, ArgumentParser)



def test_password_pwnage(capsys):
    # set test password
    test_password = 'password123'

    # testing method
    pwnage.password_pwnage(test_password)

    # capture stdout
    captured = capsys.readouterr()

    # check contents
    assert captured.out.startswith('This password has ')



def test_account_pwnage(capsys):
    # set test account
    test_account = 'ChunkyLover53@aol.com'

    # testing method
    pwnage.account_pwnage(test_account)

    # capture stdout
    captured = capsys.readouterr()

    # check contents
    assert captured.out.startswith(test_account + ' has been pwned in these breaches:')



