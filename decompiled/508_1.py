# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 508_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 573 bytes
import pickle

def unsafe_loads(serialized_data):
    return pickle.loads(serialized_data)


if __name__ == "__main__":
    serialized_data = b'...'
    try:
        data = unsafe_loads(serialized_data)
        print("Data loaded successfully:", data)
    except Exception as e:
        try:
            print("Failed to load data:", e)
        finally:
            e = None
            del e

# okay decompiling 508_1.pyc