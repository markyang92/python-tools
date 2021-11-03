#!/usr/bin/env python3
import sys

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    num_list = list(map(int, readl().split())) 
    return N, num_list 

def replaceZeroWithAnother(num_list: list, idx: int):
    start_idx=idx+1
    end_idx=-1
    for i in range(start_idx,len(num_list)):
        if num_list[i] != 0:
            start_idx=i
            # Get nums of same value in list
            for j in range(i+1,len(num_list)):
                if num_list[j]!=num_list[i]:
                    end_idx=j
                    break
            break
    temp=num_list[start_idx]
    num_list[idx]=temp
    num_list[start_idx]=0
    return num_list



if __name__ == '__main__':
    sol = 0 
    N, num_list = input_data()
    num_list=sorted(num_list)
    len_num_list=len(num_list)
    if num_list[0] == 0:
        num_list=replaceZeroWithAnother(num_list,0)
    if num_list[1] == 0:
        num_list=replaceZeroWithAnother(num_list,1)


    A=""
    B=""
    num_of_int=len_num_list//2
    for i in range(0,len_num_list):
        if i % 2 == 0:
            A+=str(num_list[i])
        else:
            B+=str(num_list[i])
    A=int(A) 
    B=int(B)
    sol=A+B
    print(sol) 
