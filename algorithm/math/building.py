#!/usr/bin/env python3
import sys

maps=[]
HIGHEST=0
HIGHEST_POINT=-1

def getCeiling():
    global maps, HIGHEST, HIGHEST_POINT
    l_top=0
    l_top_p=0
    l_width=0
    i=0
    while True:
        now_p, now_h=maps[i]
        if now_h > l_top:
            l_width+=(now_p-l_top_p)*(l_top)
            l_top=now_h
            l_top_p=now_p

        if now_p == HIGHEST_POINT:
            break
        i+=1

    r_width=0
    r_top=0
    r_top_p=0
    i=-1
    while True:
        now_p, now_h=maps[i]
        if now_h > r_top:
            r_width+=((r_top_p+1)-(now_p+1))*(r_top)
            r_top=now_h
            r_top_p=now_p
        if now_p == HIGHEST_POINT:
            break
        i=i-1

    print(HIGHEST+l_width+r_width)

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())

    for i in range(N):
        x,y=readl().strip().split()
        x=int(x)
        y=int(y)
        maps.append((x,y))
        if y > HIGHEST:
            HIGHEST=y
            HIGHEST_POINT=x
    maps=sorted(maps,key=lambda x: x[0])
    getCeiling()