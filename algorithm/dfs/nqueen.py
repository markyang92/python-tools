#!/usr/bin/env python3
import sys

N=None
dx=[1,1,1]
dy=[0,-1,1]
cnt=0

def do_Block(row: int, col: int, maps):
    global N, dx, dy
    for i in range(0,len(dx)):
        nx=row
        ny=col
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if nx < 0 or nx >= N:
                break
            if ny < 0 or ny >= N:
                break
            maps[nx][ny]+=1

def do_UnBlock(row: int, col: int, maps):
    global N, dx, dy
    for i in range(0,len(dx)):
        nx=row
        ny=col
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if nx < 0 or nx >= N:
                break
            if ny < 0 or ny >= N:
                break
            maps[nx][ny]-=1
    
def nQueen(row: int, col: int, maps):
    global N,cnt
    # row, col -> Queen
    if row == N-1:
        cnt+=1
        return
    for j in range(0,N):
        if maps[row+1][j] != 0:
            continue
        do_Block(row+1,j,maps) 
        nQueen(row+1,j,maps)
        do_UnBlock(row+1,j,maps) 


def solve(maps):
    global N
    for j in range(0,N):
        do_Block(0,j,maps) 
        nQueen(0,j,maps) # row:0, col: 0~N-1
        do_UnBlock(0,j,maps) 


if __name__ == '__main__':
    N=4
    maps=[]
    for i in range(0,N):
        maps.append([])
        maps[i]=[0]*N
    solve(maps)
    print(cnt)


