#!/usr/bin/env python3
import sys

A_LEN=None
A=[0]
F_LEN=None
F=None

def binary_search(left:int, right:int, value:int):
    if left>right:
        return 0
    mid=int((right+left)/2)
    if A[mid] < value:
        return binary_search(mid+1,right,value)
    elif A[mid] == value:
        return mid+1
    elif value < A[mid]:
        return binary_search(left,mid-1,value)


if __name__ == '__main__':
    readl=sys.stdin.readline
    A_LEN=int(readl())
    A=list(map(int,readl().split()))
    F_LEN=int(readl())
    F=list(map(int,readl().split()))
    for i in range(0,F_LEN):
        print(binary_search(0,A_LEN-1,F[i]))
