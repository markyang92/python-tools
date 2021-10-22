#!/usr/bin/env python3

M=6
N=3
comb_list=[0]*N

def comb_of_repetition(value: int, idx: int):
    comb_list[idx]=value
    if idx == N-1:
        print(*comb_list)
        return None

    for i in range(0,M):
        if comb_list[idx] <= i+1:
            comb_of_repetition(i+1,idx+1)

    

if __name__ == '__main__':
    for i in range(0,M):
        comb_of_repetition(i+1, 0)