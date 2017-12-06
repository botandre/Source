#!/usr/bin/python3

import sys

def hello():
    if(len(sys.argv) < 2):
        print("Hello, World")
    else:
        print("Hello, {}".format(sys.argv[1]))

hello()
