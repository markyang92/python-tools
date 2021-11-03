#!/usr/bin/env python3
import sys
import heapq


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [float(readl()) for _ in range(N)]
    return N, num

if __name__ == '__main__':
    N, num = input_data()
    # 입력받는 부분
    res=num[0]
    for i in range(1,N):
        if num[i]*num[i-1] >= num[i]:
            num[i]=num[i-1]*num[i]
        res=max(res,num[i])

    print(f"{res:.3f}") 