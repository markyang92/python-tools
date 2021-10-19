#!/usr/bin/env python3
import sys

N_LIST=[]

def gen(N:int):
    for i in range(1,N+1):
        for j in range(1,i):
            yield N_LIST.append((f'{j}/{i}',j/i))

def gen(arg_list: list):
    for i in len(arg_list):
        yield arg_list[i]


def iamGenerator(N: int):


if __name__ == '__main__':
    for i in iamGenerator(10):


    """
    readl=sys.stdin.readline
    N=int(readl())
    for i in gen(N):
        pass
    print(N_LIST)
    N_LIST=sorted(N_LIST,key=lambda x: x[1])

    for i in xrange(10):
        print(i)
    """

