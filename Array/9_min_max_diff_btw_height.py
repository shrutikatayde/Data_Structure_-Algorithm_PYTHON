#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        # arr.sort()
        # current_diff= arr[n-1]-arr[0]
        # for i in range(1, n-1):
        #     maxi_h=max(arr[n-1]-k, arr[i-1]+k)
        #     mini_h=min(arr[0]+k, arr[i]-1)
        # return min(current_diff, maxi_h-mini_h)
        
        n = len(arr)
    
    # Sort the array
        arr.sort()
    
    # Initialize min_diff with the difference of the current tallest and shortest tower
        min_diff = arr[n - 1] - arr[0]
    
    # Iterate through the array and consider each tower as a potential candidate
        for i in range(1, n):
        # Calculate new heights after adding or subtracting k
            min_height = min(arr[0] + k, arr[i] - k)
            max_height = max(arr[n - 1] - k, arr[i - 1] + k)
        
        # Update min_diff
            min_diff = min(min_diff, max_height - min_height)
    
        return min_diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends