#!/usr/bin/env python3
import sys

N=None
A=None

def q_sort(left: int, right: int):
    if left >= right:
        return
    P=right
    mark=left
    for j in range(mark, P):
        if A[j] < A[P]:
            if j != mark:
                temp=A[mark]
                A[mark]=A[j]
                A[j]=temp
            mark+=1

    if P != mark:
        temp=A[P]
        A[P]=A[mark]
        A[mark]=temp
    q_sort(left,mark-1)
    q_sort(mark+1,right)

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=list(map(int,readl().split()))
    q_sort(0,N-1)
    print(*A)
