#!/usr/bin/env python3
import sys

maps={
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '3',
    '5': '4',
    '6': '5',
    '7': '6',
    '8': '7',
    '9': '8'
}
def conv(origin: str):
    len_origin=len(origin)
    conv_res=[0]*len_origin
    if origin[0]=='4':
        conv_res[0]='3'
        for i in range(1,len_origin):
            conv_res[i]='9'
    else:
        for i in range(0,len_origin):
            conv_res[i]=maps[origin[i]]
    return conv_res

if __name__ == '__main__':
    N=sys.stdin.readline().strip()
    res=conv(N)
    print(int(''.join(res),9))