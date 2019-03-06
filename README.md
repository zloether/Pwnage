# pwnage.py
Checks passwords against [Have I Been Pwned](https://haveibeenpwned.com/)

### Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
You'll need to have Python installed in order to run `pwnage.py`. Start by downloading and installing the latest version of [Python 3](https://www.python.org/downloads/).
> *Note: pwnage.py has not been tested with Python 2 and will probably not work without changing some things.*

After Python is installed, install the *Requests* library.
```
pip install requests
```

### Installing
Download the latest version from GitHub using Git.
```
git clone https://github.com/zloether/pwnage.py.git
```
This will create a directory called *pwnage.py* and all the code will be in it.

### Usage
```
python pwnage.py --help
usage: pwnage.py [-h] [-p <password>] [-v]

Checks passwords against the Have I Been Pwned database
https://haveibeenpwned.com

optional arguments:
  -h, --help            show this help message and exit
  -p <password>, --password <password>
                        password to check against database
  -v, --verbose         verbose output, useful for debugging issues
```

Trying a bad password
```
python pwnage.py -p password
This password has been pwned 3645804 times!
```

Trying a better password
```
python pwnage.py -p "djf;hjdhfjk3;j4r436@@!"
This password has not been pwned yet.
```

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

### Acknowledgments

* [Troy Hunt](https://www.troyhunt.com/) for creating [Have I Been Pwned](https://haveibeenpwned.com/)
* [Requests: HTTP for Humans](python-requests.org/)

