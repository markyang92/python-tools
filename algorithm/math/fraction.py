#!/usr/bin/env python3
import sys

N_LIST=[]

def gen(N:int):
    global N_LIST
    insert=True
    for i in range(1,N+1):
        for j in range(1,i):
            for k in range(0, len(N_LIST)):
                if abs(N_LIST[k][1] - j/i) <= 0.0:
                    insert=False
                    break
            if insert:
                yield N_LIST.append((f'{j}/{i}',j/i))
                N_LIST=sorted(N_LIST,key=lambda x: x[1])
            insert=True

def printer():
    global N_LIST
    len_list=len(N_LIST)
    for i in range(0,len_list):
        yield N_LIST[i][0]


if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    for i in gen(N):
        pass
    print("0/1")
    for i in printer():
        print(i)
    print("1/1")