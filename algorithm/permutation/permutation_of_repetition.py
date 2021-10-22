#!/usr/bin/env python3

# Get permutation of repetition
# Dice: 6
# Nums: 3
# Big O: 6**3
# Result: (6,6,6), (6,5,5) ...

permute_list=[]
N=None
M=None

def permute(value:int, idx: int):
    global permute_list, N, M
    permute_list[idx]=value
    if idx == M-1:
        print(*permute_list)
        return None
    for i in range(0, N):
        permute(i+1,idx+1)


if __name__ == '__main__':
    N=6
    M=3
    permute_list=[0]*M
    for i in range(0,N):
        permute(i+1,0) # value: select value, idx: the idx of defined value (left idx of the value)