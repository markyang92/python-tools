#!/usr/bin/env python3
import sys
import queue

maps=[]
visited=[]
T_X=None
T_Y=None

if __name__ == '__main__':
    readl=sys.stdin.readline
    C,R=map(int,readl().strip().split())
    X, Y, T_X, T_Y=map(int,readl().strip().split())
    X-=1
    Y-=1
    T_X-=1
    T_Y-=1
    for i in range(R):
        maps.append([])
        visited.append([])
        line=readl().strip()
        maps[i]=[-1]*C
        visited[i]=[False]*C
        for j in range(C):
            maps[i][j]=line[j]
    q=queue.Queue()
    q.put_nowait((Y,X,0))
    dx=[0,0,-1,1] # x = left,right
    dy=[-1,1,0,0] # y = up, down
    while not q.empty():
        now_y, now_x, now_time=q.get_nowait()
        visited[now_y][now_x]=True
        if now_x == T_X and now_y == T_Y:
            print(now_time)
            break
        for i in range(0,4):
            nx=now_x+dx[i]
            ny=now_y+dy[i]
            if (nx < 0) or (nx >= C):
                continue
            if (ny < 0) or (ny >= R):
                continue
            if visited[ny][nx]==True: 
                continue
            if maps[ny][nx]=='1':
                continue
            q.put_nowait((ny,nx,now_time+1))
    exit(0)
