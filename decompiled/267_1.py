# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 267_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 177 bytes
import py7zr

class SevenZipFile:

    def extractall(self, path):
        with py7zr.SevenZipFile("archive.7z", mode="r") as z:
            z.extractall(path)

# okay decompiling 267_1.pyc