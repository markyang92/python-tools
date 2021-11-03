#!/usr/bin/env python3
import sys 

map_bingo=[]
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
# Up, Down, Left, Right, Up&Left, Up&Right, Down&Left, Down&Right
# 0,  1,     2,    3,      4,         5,        6,        7
BINGO_CNT=0
def input_data(): 
    global map_bingo
    readl = sys.stdin.readline 
    for i in range(0,5):
        map_bingo.append([])
        temp_list=list(map(int,readl().strip().split()))
        temp_list=[(int(i),'F')for i in temp_list]
        map_bingo[i]=temp_list
    
    seq_bingo=[]
    for _ in range(5):
        seq_bingo+=list(map(int,readl().split()))
    return map_bingo, seq_bingo


def GoUpDown(row:int, col: int):
    global map_bingo, dx, dy, BINGO_CNT
    cnt=1
    for i in [0,1]:
        nx=row
        ny=col
        while True:
            nx=nx+dx[i]
            ny=ny+dy[i]
            if nx < 0 or nx >= 5:
                break
            if map_bingo[nx][ny][1] == 'T':
                cnt+=1
                continue
            elif map_bingo[nx][ny][1] == 'F':
                break
    if cnt == 5:
        BINGO_CNT+=1

def GoLeftRight(row: int, col: int):
    global map_bingo, dx, dy, BINGO_CNT
    cnt=1
    for i in [2,3]:
        nx=row
        ny=col
        while True:
            nx=nx+dx[i]
            ny=ny+dy[i]
            if ny < 0 or ny >= 5:
                break
            if map_bingo[nx][ny][1] == 'T':
                cnt+=1
                continue
            elif map_bingo[nx][ny][1] == 'F':
                break
    if cnt == 5:
        BINGO_CNT+=1

def GoUpLeftAndDownRight(row: int, col: int):
    global map_bingo, dx, dy, BINGO_CNT
    cnt=1
    for i in [4,7]:
        nx=row
        ny=col
        while True:
            nx=nx+dx[i]
            ny=ny+dy[i]
            if nx < 0 or nx >= 5:
                break
            if ny < 0 or ny >= 5:
                break
            if map_bingo[nx][ny][1] == 'T':
                cnt+=1
                continue
            elif map_bingo[nx][ny][1] == 'F':
                break
    if cnt == 5:
        BINGO_CNT+=1

def GoUpRightAndDownLeft(row: int, col: int):
    global map_bingo, dx, dy, BINGO_CNT
    cnt=1
    for i in [5,6]:
        nx=row
        ny=col
        while True:
            nx=nx+dx[i]
            ny=ny+dy[i]
            if nx < 0 or nx >= 5:
                break
            if ny < 0 or ny >= 5:
                break
            if map_bingo[nx][ny][1] == 'T':
                cnt+=1
                continue
            elif map_bingo[nx][ny][1] == 'F':
                break
    if cnt == 5:
        BINGO_CNT+=1

def bingoChecker(row: int,col: int):
    GoUpDown(row,col)
    GoLeftRight(row,col)
    GoUpLeftAndDownRight(row,col)
    GoUpRightAndDownLeft(row,col)


def solve(now_val: int):
    global map_bingo
    # 1. Mark 
    for i in range(0,5):
        if (now_val,'F') in map_bingo[i]:
            col=map_bingo[i].index((now_val,'F'))
            map_bingo[i][col]=(now_val,'T')
            bingoChecker(i,col)
    

if __name__ == '__main__':
    sol = 0 
    # 입력받는 부분 
    map_bingo, seq_bingo = input_data() 
    # 여기서부터 작성 
    solve_cnt=0
    for i in seq_bingo:
        solve_cnt+=1
        solve(i)
        '''
        for j in range(0,5):
            print(map_bingo[j])
        print(f'BINGO_CNT: {BINGO_CNT}')
        '''
        if BINGO_CNT>=3:
            print(solve_cnt)
            exit(0)
    exit(0)
