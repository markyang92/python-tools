#!/usr/bin/env python3
import sys

def gen(N: int, string: str, str_len= int):
    char=string[0]
    cnt=1
    for i in range(1,str_len+1):
        if char != string[i]:
            if cnt >= N:
                yield f'{char}({cnt})'
            else:
                for j in range(0,cnt):
                    yield char
            cnt=1
            char=string[i]
        else:
            cnt+=1


    

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl().strip())
    string=readl().strip()
    string_len=len(string)
    for i in gen(N, string+'0', string_len):
        print(i,end='')
