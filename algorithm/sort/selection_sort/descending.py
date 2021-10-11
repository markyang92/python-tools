#!/usr/bin/env python3
import sys

def descending_sort(N: int, A: list):
    for i in range(0, N):
        if i==N-1:
            break
        for j in range(i+1, N):
            if A[i]<A[j]:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
            else:
                continue

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    if N == 0:
        exit(0)
    A=list(map(int,readl().split()))
    descending_sort(N,A)
    print(*A)