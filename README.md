# pwnage.py
[![Python](https://img.shields.io/badge/python-v3.5+-blue.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/zloether/pwnage.py.svg?branch=master)](https://travis-ci.org/zloether/pwnage.py)
[![Issues](https://img.shields.io/github/issues/zloether/pwnage.py.svg)](https://github.com/zloether/pwnage.py/issues)
[![License](https://img.shields.io/github/license/zloether/pwnage.py.svg)](https://opensource.org/licenses/MIT)

Python based command line tool for checking the [Have I Been Pwned](https://haveibeenpwned.com/) database.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
You'll need to have Python installed in order to run `pwnage.py`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: `pwnage.py` has not been tested with Python 2 and will probably not work without changing some things.*

After Python is installed, install the *requests* library.
```
pip install requests
```

## Installation
Download the latest version from GitHub using Git.
```
git clone https://github.com/zloether/pwnage.py.git
```
This will create a directory called *pwnage.py* and all the code will be in it.

## Usage
```
python pwnage.py -h
usage: pwnage.py [-h] [-a <account>] [-p <password>] [-r] [-v]

Checks passwords against the Have I Been Pwned database
https://haveibeenpwned.com

optional arguments:
  -h, --help            show this help message and exit
  -a <account>, --account <account>
                        account to check against database
  -p <password>, --password <password>
                        password to check against database
  -r, --prompt          prompt for pass to check against database
  -v, --verbose         verbose output, useful for debugging issues

optional arguments '-p/--password' and '-r/--prompt' cannot be used together
```

Checking an account
```
python pwnage.py --account Zoidberg@freemail.web
Zoidberg@freemail.web has been pwned in these breaches:
Unverified: Collection1 on 2019-01-07. Details leaked: Email addresses, Passwords
Verified: VK on 2012-01-01. Details leaked: Email addresses, Names, Passwords, Phone numbers
```

Trying a bad password
```
python pwnage.py --password Password1234
This password has been pwned 3621 times!
```

Trying a better password
```
python pwnage.py --password "djf;hjdhfjk3;j4r436@@!"
This password has not been pwned yet.
```

Getting prompted for a password
```
python pwnage.py --prompt
Password to check:
This password has been pwned 21961 times!
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [Troy Hunt](https://www.troyhunt.com/) for creating [Have I Been Pwned](https://haveibeenpwned.com/)
* [Requests: HTTP for Humans](http://python-requests.org/)

