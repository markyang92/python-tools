#!/usr/bin/env python3
import sys 

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    num = [int(readl()) for _ in range(N)] 
    return N, num 

def ret_sum(num: int):
    return sum([int(x) for x in str(num)])

if __name__ == '__main__':
    sol = 0 

    N, num = input_data() 

    max_sum=-sys.maxsize
    max_sum_int=None
    for i in range(0,N):
        now_num_origin=num[i]
        now_num=now_num_origin
        now_sum=0
        while True:
            now_sum=ret_sum(now_num)
            if len(str(now_sum)) != 1:
                now_num=now_sum
            else:
                if max_sum < now_sum:
                    max_sum=now_sum
                    max_sum_int=now_num_origin
                elif max_sum == now_sum:
                    if max_sum_int > now_num_origin:
                        max_sum_int=now_num_origin
                break

    print(max_sum_int)
