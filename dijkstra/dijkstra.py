#!/usr/bin/env python3
import sys
import heapq

if __name__ == '__main__':
    readl=sys.stdin.readline
    V,E=map(int,readl().strip().split())
    # create map graph
    maps=[ dict() for _ in range(V+1) ]
    for i in range(0,E):
        V1, V2, cost=map(int, readl().strip().split())
        maps[V1].update({V2:cost})

    start=1

    # create dist list
    dist=[float('inf')]*(V+1)

    dist[start]=0
    
    print(f'dist: {dist}') 
    pq=[]
    heapq.heappush(pq,(dist[start],start))
                    # (weight, to)

    while pq:
        sig_weight, now = heapq.heappop(pq)
        if sig_weight > dist[now]: continue
        for to in maps[now].keys():
            if sig_weight+maps[now][to] < dist[to]:
                dist[to]=sig_weight+maps[now][to]
                heapq.heappush(pq,(dist[to],to))
    print(f'dist: {dist}') 
