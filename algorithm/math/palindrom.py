#!/usr/bin/env python3
import sys

def isPalindrome(num: int):
    num_str=str(num)
    num_len=len(num_str)
    length=int(num_len/2)
    for i in range(0, length):
        if num_str[i] == num_str[-i-1]:
            continue
        else:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl().strip())
    for i in range(0,N):
        num=readl().strip()
        num_len=len(num)
        reversed_num=''
        for j in range(-1,-num_len-1,-1):
            reversed_num=reversed_num+num[j]
        added_num=int(num)+int(reversed_num)
        print(isPalindrome(added_num))
    exit(0)
        

