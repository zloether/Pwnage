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
    assert True