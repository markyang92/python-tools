#!/usr/bin/env python3

def gen():
    for i in range(10):
        yield i**3


if __name__ == '__main__':
    ret=gen()
    print(ret.__repr__)