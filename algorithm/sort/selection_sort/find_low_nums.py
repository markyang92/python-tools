#!/usr/bin/env python3
import sys
GET_NUMS=4 # How many numbers that you want to get it from Array A, in your standard.

def ascending_sort(N:int, A:list):
    for i in range(0,N):
        if i == N-1:
            break
        if i == GET_NUMS:
            break
        for j in range(i+1,N):
            if A[i] > A[j]:
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
            else:
                continue

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=list(map(int,readl().split()))
    ascending_sort(N,A)
    print(*A[0:GET_NUMS])