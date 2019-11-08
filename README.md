# python-password-gen
Simple console application for generating password using md5 hashing and python

## Usage

This simple application takes in a couple of user prompts and a password and returns a 32 character password generated from the md5 hash plus a couple of arbitrary rules for choosing characters to capitalize or replace with special characters, if the user so chooses.

First, install [pyperclip](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/) and ensure you have the requirements for your os.
```bash
pip install pyperclip
```

Then, run with the below:
```bash
python3 pass-gen.py
```

Follow the prompts and copy the result.

### Notes

This is far from robust, and not intended to be used in place of a properly encrypted password in a database. It does however provide you with some protection from brute force attacks, and provide you with some minor protection in the case of a data breach of any given website, assuming you re-use passwords.

For instance, a password of `password` and site of `facebook` will generate a different value than `password` and `gmail`. Thus, if one website is compromised, only that one log-in is in jeopardy.
