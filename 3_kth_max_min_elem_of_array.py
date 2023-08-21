# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 11:41:35 2023

@author: Lenovo
"""

# User function Template for python3


class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
#for Kth maximum element 
        for i in range(0, r):
            arr.sort(reverse=False)
            return arr[k-1]
#for Kth minimum element      
        for i in range(0, r):
            arr.sort(reverse=True)
            return arr[k-1]
        # {
 # Driver Code Starts
# Initial Template for Python 3


# contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))

# } Driver Code Ends
