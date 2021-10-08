#!/usr/bin/env python3
import sys

def ascending_sort(N:int, A:list):
    for i in range(0,N):
        for j in range(i+1,N):
            try:
                if A[j]>A[i]:
                    continue
                else:
                    temp=A[i]
                    A[i]=A[j]
                    A[j]=temp
            except:
                pass



if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=list(map(int,readl().split()))
    ascending_sort(N,A)
    print(*A)

