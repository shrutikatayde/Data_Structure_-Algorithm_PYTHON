# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 12:06:54 2023

@author: Lenovo
"""

def sort012(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    
    for ele in arr:
        if ele==0:
            count0+=1
        elif ele==1:
            count1+=1
        elif ele==2:
            count2+=1
    
    i=0
    while count0>0:
        arr[i]=0
        i+=1
        count0-=1
    while count1>0:
        arr[i]=1
        i+=1
        count1-=1
    while count2>0:
        arr[i]=2
        i+=1
        count2-=1
 

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input("Enter the array: elements should be 0 1 and 2 \n").split()))
        sort012(arr)
        result = ' '.join(map(str,arr))
        print(result)
