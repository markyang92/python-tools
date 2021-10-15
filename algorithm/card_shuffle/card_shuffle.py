#!/usr/bin/env python3

import sys

N=None
CARD=None

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    CARD=[i+1 for i in range(N)]

    last_idx=-1
    while True:
        last_card=CARD[last_idx]
        shuffle=int(last_card/2)
        last_idx=last_idx+shuffle
        last_idx=last_idx+1 # Makes last_idx to front_idx temporarily
        while True:
            if last_idx < N:
                break
            last_idx=last_idx%N
        print(CARD[last_idx],end=' ')
        del CARD[last_idx]
        last_idx=last_idx-1
        N-=1
        if N == 0:
            break