#!/usr/bin/env python3
import sys

N=None
S=None
VALUE=None
NOW_LIST=None
SOLVED=False

def getResult(value: int, sum: int):
    global N,S,VALUE, NOW_LIST, SOLVED
    sum=sum+value
    if sum == S:
        SOLVED=True
        print("YES")
        return
    if sum > S:
        return
    for i in range(0,N):
        if (VALUE[i] > value) and (NOW_LIST[VALUE[i]] == False):
            NOW_LIST[VALUE[i]]=True
            getResult(VALUE[i],sum)
            if SOLVED:
                return
            NOW_LIST[VALUE[i]]=False

def Solve():
    global N,S,VALUE, NOW_LIST
    for i in range(0,N):
        NOW_LIST[VALUE[i]]=True
        getResult(VALUE[i],0)
        if SOLVED:
            break
        NOW_LIST[VALUE[i]]=False

if __name__ == '__main__':
    readl=sys.stdin.readline
    T=int(readl().strip())
    for i in range(0,T):
        N, S=map(int,readl().strip().split())
        VALUE=list(map(int,readl().strip().split()))
        NOW_LIST=dict()
        for j in range(0,N):
            NOW_LIST[VALUE[j]]=False
        Solve()
        if not SOLVED:
            print("NO")
        SOLVED=False
        VALUE.clear()
        NOW_LIST.clear()