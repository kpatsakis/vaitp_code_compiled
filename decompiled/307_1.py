# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 307_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 405 bytes
import subprocess

def execute_untrusted_code(code):
    exec(code)


if __name__ == "__main__":
    untrusted_code = "print('This code is executed!')"
    execute_untrusted_code(untrusted_code)

# okay decompiling 307_1.pyc