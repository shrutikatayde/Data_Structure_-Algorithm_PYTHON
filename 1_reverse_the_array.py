
#--------REVERSE THE ARRAY------------

#--->> METHOD 1--> BY USING SLICING

arr= list(map(int, input("Enter the array:").split()))
b=arr[::-1]
rev_str = ' '.join(map(str,b))
print (rev_str)
print(type(rev_str))

'''Time Complexity: O(n) + O(n) + O(n) = O(n)
   Space Complexity: O(n) + O(n) + O(n) = O(n) '''

#--->> METHOD 2'  -->> BY RECURSION

def rev_arr(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end]=arr[end], arr[start]
    rev_arr(arr, start+1, end-1)
         
n=int(input("Enter the size of array : "))
arr= list(map(int, input("Enter the array : ").split()))

rev_arr(arr, 0, n-1)
rev_str = ' '.join(map(str,arr))
print("Reversed array :" , rev_str)

'''Time Complexity: O(n)
   Auxiliary Space: O(n), due to recursive call stack'''

#--->> METHOD 3 -->> BY ITERATION

def rev_arr(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
         
n=int(input("Enter the size of array : "))
arr= list(map(int, input("Enter the array : ").split()))

rev_arr(arr, 0, n-1)
rev_str = ' '.join(map(str,arr))
print("Reversed array :" , rev_str)

'''Time Complexity: O(n)
   Auxiliary Space: O(1)'''

'''for element in arr:
    print(element, end=" ")  #for removing brackets'''






