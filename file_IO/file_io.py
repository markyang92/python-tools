#!/usr/bin/env python3

import sys

if __name__=='__main__':
    f=open('sample','r')

    for line in f:
        print(line)
    
    f.close()