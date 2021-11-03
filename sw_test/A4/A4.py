#!/usr/bin/env python3
import sys
def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    return N 

def get_happy_num(num: str):
    sum=0
    for i in range(0, len(num)):
        sum+=int(num[i])**2
    return sum



if __name__ == '__main__':
    sol = 0 
    N = input_data()
    find_happy=False
    for i in range(N,0,-1):
        now_num=i
        hash_table=dict()
        hash_table[now_num]=True
        while True:
            now_num_str=str(now_num)
            now_res=get_happy_num(now_num_str)
            #print(f'now_num: {now_num}, now_res: {now_res}, hash_table[now_res]: {hash_table.get(now_res)}')
            if hash_table.get(now_res) == True:
                break
            elif now_res != 1:
                now_num=now_res
                hash_table[now_res]=True
            elif now_res == 1:
                sol=i
                find_happy=True
                hash_table.clear()
                break
        if find_happy:
            break



    print(i)