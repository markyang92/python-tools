#!/usr/bin/env python3
import sys

def input_data(): 
    readl = sys.stdin.readline 
    K = int(readl()) 
    N = int(readl()) 
    info = [readl().split() for _ in range(N)] 
    info = [(int(t), z) for t,z in info] 
    return K, N, info 

# 입력받는 부분 
if __name__ == '__main__':
    K, N, info = input_data() 

    time=0
    bomb_idx=K-1

    for i in range(0,N):
        time+=info[i][0]
        if time >= 210:
            break
        if info[i][1] == 'T':
            bomb_idx+=1
            if bomb_idx>=8:
                bomb_idx=bomb_idx%8
        i+=1
    print(bomb_idx+1)