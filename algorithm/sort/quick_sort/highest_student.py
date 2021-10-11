#!/usr/bin/env python3
import sys
N=None
A=None

HIGHEST_NUM=3   # Students who get high score in the upper #th.
cnt=0
def q_sort(left:int, right: int):
    if left >= right:
        return
    p=right # Pivot
    mark=left
    for j in range(mark,p):
        if (A[j][0] < A[p][0]) or ((A[j][0] == A[p][0]) and (A[j][1] > A[p][1])):
            if (j != mark):
                temp=A[mark]
                A[mark]=A[j]
                A[j]=temp
            mark+=1

    if p != mark:
        temp=A[p]
        A[p]=A[mark]
        A[mark]=temp

    print(A[mark])
    q_sort(left,mark-1)
    q_sort(mark+1,right)
    

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=readl().split()
    for idx,val in enumerate(A):
        A[idx]=(int(val),idx+1)
    print(f'before: A: {A}')
    q_sort(0,N-1)
    print(f'After: A: {A}')
    for i in range(0,HIGHEST_NUM):
        print(A[i][1],end=' ')
