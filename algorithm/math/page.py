#!/usr/bin/env python3
import sys

N=None
Page=None
Book=None
result=[]

def pickPage():
    mid=int(N/2)
    magic_number=N+1
    result.append(magic_number-Page)
    if Page%2 == 0:
        result.append(Page-1)
        result.append(magic_number-(Page-1))
    else:
        result.append(Page+1)
        result.append(magic_number-(Page+1))

if __name__ == '__main__':
    readl=sys.stdin.readline
    stdin=readl().split()
    N=int(stdin[0])
    Page=int(stdin[1])
    Book=[i for i in range(1,N+1)]
    pickPage()
    print(*sorted(result))