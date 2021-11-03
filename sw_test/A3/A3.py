#!/usr/bin/env python3
import sys

def calc(num: int,N:int, P: int):
    return (num*N)%P


if __name__ == '__main__':
    readl=sys.stdin.readline
    N, P=map(int,readl().strip().split())
    now_num=N
    hash_table=dict()
    while True:
        ret=calc(now_num,N,P)
        if hash_table.get(ret) == None:
            hash_table[ret]=True
        elif hash_table.get(ret) == True:
            print(len(hash_table))
            break
        now_num=ret
