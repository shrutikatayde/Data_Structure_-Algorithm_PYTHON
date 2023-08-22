# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:50:40 2023

@author: Lenovo
"""

#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        count=len(set(a+b))

        return count
    
    ''' a.extend(b)
        s=set(a)
        return len(s)'''

'''     s1=set(a)
        s2=set(b)
        ans=s1|s2
        return len(ans)'''
    
'''     l=list(set(a)|set(b))
        c=0
        for i in range(len(l)):
            c+=1
        return c'''

#{ 
# Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends