# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1126_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 183 bytes


def get_redirect_url(redirect_url):
    return redirect_url


malicious_redirect = "https://attacker.com"
print("Redirecting to:", get_redirect_url(malicious_redirect))

# okay decompiling 1126_1.pyc
