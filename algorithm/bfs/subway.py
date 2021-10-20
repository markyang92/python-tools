#!/usr/bin/env python3
import sys
import queue
MIN=float('inf')

if __name__ == '__main__':
	readl=sys.stdin.readline
	N,M=map(int,readl().strip().split()) # N: The nums of subway station, M: Wanted numer of the station
	# Map N*N
	maps=[]
	for i in range(N):
		maps.append([])
		line=list(map(int,readl().strip().split()))
		maps[i]=line

	visited=[float('inf')]*(N)
	route=[0]*N
	q=queue.Queue()
	q.put_nowait((0,-1,0)) # Location, before Location, time
	while not q.empty():
		now, before, now_time =q.get_nowait()
		if visited[now]>now_time:
			visited[now]=now_time
			route[now]=before
		for i in range(N):
			if now==i:
				continue
			if visited[i] > now_time+maps[now][i]:
				q.put_nowait((i,now,now_time+maps[now][i]))
	print(visited[M-1])
	path_list=[]
	path_list.append(M)
	idx=M-1
	while True:
		path_list.insert(0,route[idx]+1)
		idx=route[idx]
		if route[idx] == -1:
			break
	print(*path_list)
	exit(0)