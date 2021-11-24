#!/usr/bin/env python3
import heapq

if __name__ == '__main__':
    pq=[]
    heapq.heappush(pq,(1,{'name': 'yang', 'score': 92}))
    heapq.heappush(pq,(0,{'name': 'kim', 'score': 90}))
    print(heapq.heappop(pq))
    print(heapq.heappop(pq))


