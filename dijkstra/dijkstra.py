#!/usr/bin/env python3
import sys
import heapq

maps=None
dist=None
visited=None
V=None

def find_shortest_node():
    global maps,dist,visited,V
    min_dist=float('inf')
    min_idx=-1
    for i in range(1,V+1):
        if visited[i] == True: continue
        if dist[i] < min_dist:
            min_dist=dist[i]
            min_idx=i
    return min_idx

def update_dist(new_node: int):
    global maps,dist,visited,V
    for i in range(1,V+1):
        if visited[i] == True: continue
        if dist[i] > dist[new_node] + maps[new_node][i]:
            dist[i]=dist[new_node]+maps[new_node][i]


if __name__ == '__main__':
    readl=sys.stdin.readline
    V,E=map(int,readl().strip().split())
    # create map graph
    maps=[ dict() for _ in range(V+1) ]
    for i in range(0,E):
        V1, V2, cost=map(int, readl().strip().split())
        maps[V1].update({V2:cost})

    print(maps)
    # create dist list
    dist=[float('inf')]*(V+1)
    # create visited list
    visited=[False]*(V+1)

    # select start node
    start=1
    for key in maps[start].keys():
        dist[key]=maps[start][key]
    print(dist)
    exit(0)
    dist[start]=0
    visited[start]=True
    print(f'dist: {dist}') 
    print(f'visited: {visited}') 
    for i in range(0,V-1):
        new_node=find_shortest_node()
        visited[new_node]=True
        update_dist(new_node)
    
    print(dist)
    print(visited)
