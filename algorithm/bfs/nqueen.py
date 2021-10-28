#!/usr/bin/env python3
import sys

N=None
maps=None
dx=[1,1,1] # up,up,up
dy=[0,-1,1] # -,left,right

def check(row: int, col: int, idx: int):
    nx=row+dx[idx]
    ny=col+dy[idx]
    if nx < 0 or nx >= N:
        return False
    if ny < 0 or ny >= N:
        return False
    if maps[nx][ny] == 1:
        return False



def solve():
    global N,maps,dx,dy
    for i in range(0,N):
        for j in range(0,N):
            maps[i][j]=1
            check(i,j)
            nqueen(0+1,j)
            maps[i][j]=0

if __name__ == '__main__':
    #N=int(sys.stdin.readline().strip())
    N=4
    maps=[]
    for i in range(0,N):
        maps.append([])
        maps[i]=[0]*N
    solve()
    
