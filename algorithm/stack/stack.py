#!/usr/bin/env python3
import sys

N=None
A=None

class Stack():
    def __init__(self, size: int):
        self.max_size=size
        self.stack_list=[None]*self.max_size
        self.cur_size=0
        self.sp=-1
    
    def pop(self):
        if self.cur_size == 0:
            return -1
        ret=self.stack_list[self.sp]
        self.stack_list[self.sp]=None
        self.sp-=1
        self.cur_size-=1
        return ret
    
    def push(self, push_item: int):
        if self.cur_size >= self.max_size:
            return -1
        self.sp+=1
        self.stack_list[self.sp]=push_item
        self.cur_size+=1
        return 0
        
if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl())
    A=list(map(int,readl().split()))
    stack=Stack(4)
    for i in range(0,N):
        if A[i] == 0:
            # Pop!
            ret=stack.pop()
            print(ret,end=' ')
        else:
            # Push!
            ret=stack.push(A[i])
            if ret == -1:
                print(ret,end=' ')
