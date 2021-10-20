#!/usr/bin/env python3
import sys
import queue

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=list(map(int,readl().strip().split()))
    V=N[0]+1 # vertex
    E=N[1] # edge
    # vertex: 1~V
    maps=[]
    visited=[]
    for i in range(0,V):
        maps.append([])
        visited.append(False)
    for i in range(0,E):
        get_str=list(map(int,readl().strip().split()))
        start=get_str[0]
        end=get_str[1]
        maps[start].append(end)
    
    Q=queue.Queue()
    Q.put_nowait(1)
    while not Q.empty():
        now_v=Q.get_nowait()
        if visited[now_v]:
            continue
        print(now_v,end=' ')
        visited[now_v]=True
        for i in range(len(maps[now_v])):
            if not visited[maps[now_v][i]]:
                Q.put_nowait(maps[now_v][i])
    
    for i in range(1,len(visited)):
        if visited[i]==False:
            print(i,end=' ')
