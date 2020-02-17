"""
Read a file from a location on your computer
"""

import os
path = os.path.join("/home",
             "tde1224",
             "Documents",
             "test.txt")

with open(path, "r") as f:
    print(f.read())

