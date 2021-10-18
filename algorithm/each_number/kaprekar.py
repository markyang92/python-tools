#!/usr/bin/env python3

import sys

def toBiggest(num_list: list):
    ret=[]
    sorted(num_list)
    print(num_list)



def toDecimal(X: int):
    nums=[]
    X_copy=X
    while True:
        num=X_copy%10
        nums.append(num)
        X_copy=int(X_copy/10)
        if X_copy == 0:
            break
    
    return nums

if __name__ == '__main__':
    readl=sys.stdin.readline
    #X=int(readl())
    X=1789
    nums=toDecimal(X)
    nums.sort()
    smallest=''
    biggest=''
    for i in range(0, len(nums)):
        smallest=smallest+str(nums[i])
        biggest=str(nums[i])+biggest

    print(smallest)
    print(biggest)

