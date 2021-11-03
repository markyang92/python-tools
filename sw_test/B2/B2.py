#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    stack=list(sys.stdin.readline().strip())
    cnt=0
    if stack[0]==')':
        cnt+=1
        stack[0]='('
    if stack[-1]=='(':
        cnt+=1
        stack[-1]=')'
    # left= )
    # right= (
    bal=0
    for i in range(0,len(stack)):
        if stack[i] == '(':
            bal+=1
        elif stack[i] == ')':
            bal-=1
        if bal < 0:
            stack[i]='('
            bal=1
            cnt+=1
    if bal > 0:
        cnt=cnt+bal//2
    # balance must be end == '0'
    print(cnt)
        