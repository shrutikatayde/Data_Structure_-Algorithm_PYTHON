# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:04:06 2023

@author: Lenovo
"""
# METHOD 1
'''def move_neg_ele(arr, n):
    result=arr.sort()
    return result

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input("Enter the array: both -ve and +ve \n").split()))
        move_neg_ele(arr, n)
        result = ' '.join(map(str,arr))
        print(result)'''
        
'''Time Complexity: O(n*log(n)), Where n is the length of the given array.
   Auxiliary Space: O(1)'''

# METHOD 2

'''def move(arr, left, right):
    
    while left<=right:
        
        if arr[left]<arr[right] and arr[right]<arr[left]:
            left+=1
        
        elif arr[left]> arr[right] and arr[right]<arr[left]:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
        elif arr[left]> arr[right] and arr[right]> arr[left]:
            right-=1
        else:
            left-=1
            right-=1  
    

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input("Enter the array: both -ve and +ve \n").split()))
        move(arr, 0, n-1)
        result = ' '.join(map(str,arr))
        print(result)'''
'''Time Complexity: O(N)
   Auxiliary Space: O(1)'''


# METHOD 3
def rearrange(arr, start, end):
    while start<end:
        if arr[start]<0:
            start+=1
        elif arr[end]>0:
            end-=1
        else:
            arr[start], arr[end]=arr[end],arr[start]
 
def printarray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
        

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input("Enter the array: both -ve and +ve \n").split()))
        rearrange(arr, 0, n-1)
        result = ' '.join(map(str,arr))
        printarray(arr, n)
'''Time complexity: O(N) 
   Auxiliary Space: O(1)'''
