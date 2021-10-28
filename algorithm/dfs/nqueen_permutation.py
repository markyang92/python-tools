#!/usr/bin/env python3
import sys

maps=[]
N=None
cnt=0
prohibit=[]

def check(idx:int, value: int):
    global maps
    if value in maps[0:idx]:
        return False

    for i in range(0, idx):
        std=maps[i]
        if std+(1*(idx-i)) == value:
            return False
        if std-(1*(idx-i)) == value:
            return False
    return True

def prohibitMarker(idx: int, value: int):
    # idx: Now choosen index
    # value: Now choosen value
    global prohibit, N
    # Down
    for i in range(idx+1,N):
        prohibit[i].append(value)
        val1=value+(i-idx)
        val2=value-(i-idx)
        if val1 >= 0 and val1 < N:
            prohibit[i].append(val1)
        val2=value-(i-idx)
        if val2 >= 0 and val2 < N:
            prohibit[i].append(val2)
    
def prohibitCleaner(idx: int, value: int):
    global prohibit, N
    # Down
    for i in range(idx,N):
        try:
            prohibit[i].remove(value)
        except:
            pass
        val1=value+(i-idx)
        val2=value-(i-idx)
        if val1 >= 0 and val1 < N:
            try:
                prohibit[i].remove(val1)
            except:
                pass
        val2=value-(i-idx)
        if val2 >= 0 and val2 < N:
            try:
                prohibit[i].remove(val2)
            except:
                pass


def permute(idx:int, value: int):
    global maps, N, cnt
    # idx max == N-1
    if idx == N-1:
        cnt+=1
        return
    maps[idx]=value
    prohibitMarker(idx,value)
    for i in range(0,N):
        if i in prohibit[idx+1]:
            continue
        permute(idx+1,i)
        prohibitCleaner(idx+1,i)
        
def init_prohibit():
    global prohibit,N
    for i in range(0,N):
        prohibit[i]=[]
    
def solve():
    global N
    for i in range(0,N):
        init_prohibit()
        permute(idx=0,value=i)

if __name__ == '__main__':
    N=int(sys.stdin.readline().strip())
    maps=[0]*N
    prohibit=[0]*N
    solve()
    print(cnt)