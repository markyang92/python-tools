#!/usr/bin/env python3

import time


def print_function(arg1,arg2,arg3,arg4,arg5,arg6):
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")

def chronometry(f, *args, **kwargs):
    print(args)
    print(kwargs)

    start=time.time()
    f(*args,**kwargs)
    end=time.time()
    print(f'elapsed: {end-start}')


if __name__ == '__main__':

    args=("two",3,5)
    kwargs={"arg4":3, "arg5": "two", "arg6": 5}
    chronometry(print_function,*args,**kwargs)
