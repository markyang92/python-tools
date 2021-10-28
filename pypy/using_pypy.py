#!/usr/bin/env python3
import time

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

start=time.time()
fibo(40)
print(f'time: {time.time()-start}')