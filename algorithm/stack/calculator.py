#!/usr/bin/env python3
import sys
N=None
A=[]
O=[]

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    temp=readl().split()
    len_temp=len(temp)
    for i in range(0,len_temp):
        if temp[i] in ['+','-','*','/']:
            O.append(temp[i])
        else:
            A.append(int(temp[i]))
    len_O=len(O)
    i=0
    while True:
        if O[i] in ['*', '/']:
            # 1st Priority
            if O[i] == '*':
                temp=A[i]*A[i+1]
                del A[i+1]
                A[i]=temp
            elif O[i] == '/':
                temp=int(A[i]/A[i+1])
                del A[i+1]
                A[i]=temp
            del O[i]
            len_O-=1
        else:
            i+=1
        if i < len_O:
            continue
        else:
            break

    len_O=len(O)
    i=0
    while True:
        # 2st Priority '+' or '-'
        if O[i] in ['+', '-']:
            if O[i] == '+':
                temp=A[i]+A[i+1]
                del A[i+1]
                A[i]=temp
            elif O[i] == '-':
                temp=A[i]-A[i+1]
                del A[i+1]
                A[i]=temp
            del O[i]
            len_O-=1
        else:
            i+=1
        if i < len_O:
            continue
        else:
            break
    print(A[0])