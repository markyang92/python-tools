#!/usr/bin/env python3
import sys
maps=[]
R=None
C=None
CNT=0

def handshake(point: tuple):
    global maps, R, C, CNT
    r,c=point
    if maps[r][c] == 'o':
        return
    cnt=0
    for i in range(r-1,r+1+1,+1):
        if (i < 0) or (i >= R):
            continue
        for j in range(c-1,c+1+1,+1):
            if (j < 0) or (j >= C):
                continue
            if maps[i][j]=='.':
                continue
            elif maps[i][j]=='o':
                cnt+=1
                continue
    CNT+=int(cnt/2)
    

if __name__ == '__main__':
    readl=sys.stdin.readline
    from_stdin=readl().strip().split()
    R=int(from_stdin[0])
    C=int(from_stdin[1])
    #print(f'R: {R}, C: {C}')
    for i in range(R):
        maps.append(['.']*C)
        line=readl().strip()
        for j in range(C):
            maps[i][j]=line[j]

    for i in range(R):
        for j in range(C):
            handshake((i,j))

    print(CNT)
    exit(0)