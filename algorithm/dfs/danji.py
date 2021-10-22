#!/usr/bin/env python3
import sys
dx=[1,-1,0,0] # x is row
dy=[0,0,1,-1] # y is col
maps=[]
N=None
ret=[]

def gen():
    for i in range(0,len(ret)):
        yield ret[i]


def danji_dfs(x: int, y: int, cnt: int):
    global N, max_cnt
    global dx,dy
    global maps
    maps[x][y]=0
    cnt+=1
    for i in range(0,4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (nx < 0) or (nx >= N):
            continue
        if (ny < 0) or (ny >= N):
            continue
        if maps[nx][ny]==0:
            continue
        cnt=danji_dfs(nx,ny,cnt)
    return cnt



if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl().strip()) # N*N Array
    for i in range(0,N):
        maps.append([])
        line=list(readl().strip())
        maps[i]=list(map(int,line))

    danji=0
    for i in range(0,N):
        for j in range(0,N):
            if maps[i][j] == 0:
                continue
            ret.append(danji_dfs(i,j,0))
            danji+=1
    print(danji)
    ret=sorted(ret,key=lambda x: x)
    for i in gen():
        print(i)
    exit(0)