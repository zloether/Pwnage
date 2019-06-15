# Pwnage
[![Python](https://img.shields.io/badge/python-v3.5+-blue.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/zloether/Pwnage.svg?branch=master)](https://travis-ci.org/zloether/Pwnage)
[![Issues](https://img.shields.io/github/issues/zloether/Pwnage.svg)](https://github.com/zloether/Pwnage/issues)
[![License](https://img.shields.io/github/license/zloether/Pwnage.svg)](https://opensource.org/licenses/MIT)

Python based command line tool for checking the [Have I Been Pwned](https://haveibeenpwned.com/) database.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Prerequisites
You'll need to have Python installed in order to run `Pwnage`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: `Pwnage` has not been tested with Python 2 and will probably not work without changing some things.*

## Installation
```
pip install pwnage
```

## Usage
```
pwnage --help
usage: pwnage [-h] [-a <account>] [-g] [-p <password>] [-r] [-v]

Checks passwords against the Have I Been Pwned database
https://haveibeenpwned.com

optional arguments:
  -h, --help            show this help message and exit
  -a <account>, --account <account>
                        account to check against database
  -g, --generate        generate a random password that has not been
                        compromised
  -p <password>, --password <password>
                        password to check against database
  -r, --prompt          prompt for pass to check against database
  -v, --verbose         verbose output, useful for debugging issues

optional arguments '-p/--password' and '-r/--prompt' cannot be used together
```

Checking an account
```
pwnage --account Zoidberg@freemail.web
Zoidberg@freemail.web has been pwned in these breaches:
Unverified: Collection1 on 2019-01-07. Details leaked: Email addresses, Passwords
Verified: VK on 2012-01-01. Details leaked: Email addresses, Names, Passwords, Phone numbers
```

Trying a bad password
```
pwnage --password Password1234
This password has been pwned 3621 times!
```

Trying a better password
```
pwnage --password "djf;hjdhfjk3;j4r436@@!"
This password has not been pwned yet.
```

Getting prompted for a password
```
pwnage --prompt
Password to check:
This password has been pwned 21961 times!
```

Generating a random password that gets checked against HIBP to make sure it has never been compromised
```
pwnage --generate
V@0l4uMOqXgtCidqU!'gqwlmfO0igcuM
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* [Troy Hunt](https://www.troyhunt.com/) for creating [Have I Been Pwned](https://haveibeenpwned.com/)
* [Requests: HTTP for Humans](http://python-requests.org/)

