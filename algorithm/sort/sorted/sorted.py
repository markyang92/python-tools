#!/usr/bin/env python3

def compareA(item: tuple):
    return item[1]

def compareB(item: tuple):
    return item[0]

if __name__ == '__main__':
    arr=[("yang",92),("kim",38),("park",91),("apple",38)]

    # 1순위: 점수
    # 2순위: 점수가 동일할 경우 이름 사전 순
    arr=sorted(arr,key=compareB)
    for i in range(0,len(arr)):
        print(arr[i])
    print('-----------------------')
    arr=sorted(arr,key=compareA)
    for i in range(0,len(arr)):
        print(arr[i])


    d=dict()
    d['PACKAGES']="HI Hello"
    print(d.get('PACKAGES'))