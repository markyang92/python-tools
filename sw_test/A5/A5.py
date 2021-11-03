#!/usr/bin/env python3
import sys
N=None
res=[]
std_value=None
left_val=None
res_MIN=sys.maxsize
res_MAX=-sys.maxsize
def comb_repet(idx: int, value: int):
    global res,N,std_value,left_val,res_MIN,res_MAX
    res[idx]=value
    if idx == N-1:
        now_sum=sum(res)
        if now_sum < res_MIN:
            res_MIN=now_sum
        if now_sum > res_MAX:
            res_MAX=now_sum
        return
    for i in range(value,value+2):
        if not value <= i:
            continue
        if idx+1 == N-1 and sum(res[1:idx+1])+i != left_val:
            continue
        comb_repet(idx+1,i)


if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl().strip())
    left_val=int(readl().strip())
    if left_val%(N-1) == 0:
        std_value=int((left_val/(N-1))-1)
    else:
        std_value=int((left_val/(N-1)))
    res=[0]*N
    for i in range(std_value,std_value+2):
        comb_repet(0,i)
    print(f'{res_MIN} {res_MAX}')