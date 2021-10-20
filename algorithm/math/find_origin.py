#!/usr/bin/env python3
import sys

NUMS=[]

def findOrigin(X):
    X_1='1'+X
    int_X_1=int(X_1)
    result_X_1=int(int_X_1/11)

    X_10='10'+X
    int_X_10=int(X_10)
    result_X_10=int(int_X_10/11)

    if result_X_1 < result_X_10:
        print(result_X_1)
    else:
        print(result_X_10)

if __name__ == '__main__':
    readl=sys.stdin.readline
    while True:
        now_num=readl().strip()
        if now_num == '0':
            break
        NUMS.append(now_num)

    for i in range(0,len(NUMS)):
        findOrigin(NUMS[i])

    

