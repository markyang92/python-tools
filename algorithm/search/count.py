#!/usr/bin/env python3
import sys

N=None
A=[-1]
M=None
F=[-1]

def count(start,value,cnt):
    for i in range(start,-1,-1):
        if A[i] == value:
            cnt+=1
        else:
            break
    for i in range(start+1,N):
        if A[i] == value:
            cnt+=1
        else:
            break
    return cnt

def binary_search(left: int, right:int, value: int):
    if left>right:
        return 0
    mid=int((left+right)/2)
    if A[mid] < value:
        return binary_search(mid+1,right,value)
    elif A[mid] == value:
        return count(mid,value,0)
    elif value < A[mid]:
        return binary_search(left,mid-1,value)

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=list(map(int,readl().split()))
    M=int(readl())
    F=list(map(int,readl().split()))
    for i in range(0,M):
        print(binary_search(0,N-1,F[i]))