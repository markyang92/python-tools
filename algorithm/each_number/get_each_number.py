#!/usr/bin/env python3
import sys



def getEachNums(X: int):
    num=X
    decimal_list=[]
    while True:
        each_num=num%10
        decimal_list.append(each_num)
        num=int(num/10)
        if num == 0:
            break
    return decimal_list


if __name__ == '__main__':
    X=2134
    d=getEachNums(X)
    print(*d)
