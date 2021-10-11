#!/usr/bin/env python3
import sys

# Find 'GET_NUMS' Upper Nums
GET_NUMS=3

def descending_sort(N: int, A: list):
    for i in range(0,N):
        if i == N-1:
            break
        if i == 3:
            break
        for j in range(i+1,N):
            if (A[i][0] < A[j][0]) or (A[i][0] == A[j][0] and A[i][1] > A[j][1]):
                temp=A[i]
                A[i]=A[j]
                A[j]=temp
        
if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=list(map(int,readl().split()))
    A_len=len(A)
    for i in range(0,A_len):
        A[i]=(A[i],i+1)
    descending_sort(N,A)
    for i in range(0,GET_NUMS):
        print(A[i][1],end=' ')