# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 751_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 264 bytes
import os

def vulnerable_function(code):
    exec(code)


user_input = "os.system('echo Vulnerable!')"
vulnerable_function(user_input)

# okay decompiling 751_1.pyc
