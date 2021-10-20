#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    readl=sys.stdin.readline
    line=readl().strip()
    stack=[]
    line_len=len(line)
    before=False
    cnt=0
    for i in range(0,line_len):
        if line[i] == '(':
            stack.append('(')
            trigger=True
            before=False
        elif line[i] == ')':
            stack.pop()
            cnt+=len(stack)
            before=True
    print(cnt)

