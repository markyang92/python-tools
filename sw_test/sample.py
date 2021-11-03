#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    N=10
    nums=[ sys.stdin.readline().strip() for _ in range(N) ]
    nums=[ (int(i[0]),i[-1]) for i in nums]
    print(nums)