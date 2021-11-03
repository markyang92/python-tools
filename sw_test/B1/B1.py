#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    readl=sys.stdin.readline
    N=int(readl().strip())
    arr=readl().strip().split()
    arr_dict=dict()
    for i in range(0,len(arr)):
        if arr_dict.get(arr[i]) == None:
            arr_dict[arr[i]]=[i+1]
        else:
            arr_dict[arr[i]].append(i+1)
    isAllUnique=True
    for i in arr_dict.keys(): 
        try:
            val=arr_dict[i][1]
        except:
            pass
        else:
            isAllUnique=False
            print(f'{i} ',end='')
            print(*arr_dict[i])
    
    if isAllUnique:
        print('unique')