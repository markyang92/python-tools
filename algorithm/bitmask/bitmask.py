#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    readl=sys.stdin.readline
    stdin=list(map(int,readl().split()))
    X=stdin[0]
    N=stdin[1]
    X_bit=bin(X)
    magic_num=len(X_bit)-2
    magic_num=(2**magic_num)-1
    magic_num=X^magic_num
    bin_magic_num=bin(magic_num)
    len_magic_num=-(len(X_bit)-2)


    queue=list()
    queue.append([0,'0b']) # cur,None
    len_queue=1
    string='0b0'
    string[-1]=0
    print(string)
    '''
    while len_queue >=0:
        cur, bit = queue[0]
        del queue[0]
        cur-=1
        if cur >= len_magic_num:
            if bin_magic_num[cur] == '0':
                queue.append([cur,bit+'0'])
    '''
            

