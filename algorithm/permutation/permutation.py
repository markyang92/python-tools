#!/usr/bin/env python3

# General permutation
## - 1,3,2 (O)
## - 1,2,3 (O)
## - 1,2,2 (X)

M=6+1
N=3

visited=[0]*(M+1)
dice=[0]*N

def permutation(value: int, idx: int):
    dice[idx]=value
    if idx == N-1:
        print(*dice)
        return
    for i in range(1,M):
        if visited[i]==0:
            visited[i]=1
            permutation(i,idx+1)
            visited[i]=0

if __name__ == '__main__':
    for i in range(1,M):
        visited[i]=1
        permutation(i, 0)
        visited[i]=0
