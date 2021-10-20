#!/usr/bin/env python3
import sys

def getEachNums(num: int):
    num_list=[]
    num_copy=num
    while True:
        num_list.append(num_copy%10)
        num_copy=int(num_copy/10)
        if num_copy==0:
            break

    return num_list

def compare(x,y):
    if x<y:
        return True
    else:
        return False


if __name__ == '__main__':
    readl=sys.stdin.readline
    result=int(readl())
    cnt=0
    while result != 6174:
        num_list=getEachNums(result)
        cnt+=1
        sort_list=sorted(num_list)
        smallest=''
        biggest=''
        for i in range(0,len(sort_list)):
            smallest=smallest+str(sort_list[i])
            biggest=biggest+str(sort_list[-i-1])
        smallest=int(smallest)
        biggest=int(biggest)
        result=biggest-smallest
    print(cnt)