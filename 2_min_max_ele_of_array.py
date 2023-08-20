
# --------Find Min Max from the array------------

# --->> METHOD 1--> BY Function

arr0 = list(map(int, input("Enter the array:").split()))
print("max :", max(arr0))
print("min :", min(arr0))

'''Time Complexity: O(n)
   Auxiliary Space:  O(n)'''

# --->> METHOD 2'  -->> BY sort() function


def min_max(arr1):
    arr1.sort(reverse=False)
    result = {"mini": arr1[0], "maxi": arr1[-1]}
    return result


arr1 = list(map(int, input("Enter the array:").split()))
result = min_max(arr1)
print("Min :", result["mini"])
print("Max :", result["maxi"])

'''Time Complexity: O(n log n)
   Auxiliary Space:  O(1)'''

# --->> METHOD 3 -->> BY Linear search


class pair:
    def __init__(self):
        self.min = 0
        self.max = 0


def min__max(arr2: list, n: int) -> pair:
    minmax = pair()

    if n == 1:
        minmax.max = arr2[0]
        minmax.min = arr2[0]
        return minmax

    if arr2[0] > arr2[1]:
        minmax.max = arr2[0]
        minmax.min = arr2[1]
    else:
        minmax.max = arr2[1]
        minmax.min = arr2[0]

    for i in range(2, n):
        if arr2[i] > minmax.max:
            minmax.max = arr2[i]
        elif arr2[i] < minmax.min:
            minmax.min = arr2[i]

    return minmax


# Driver code
if __name__ == "__main__":
    n = int(input("Enter the size of array : "))
    arr2 = []
    for i in range(n):
        ele = input(f'Element no. {i} --> ')
        arr2.append(ele)
    minmax = min__max(arr2, n)
    print("max : ", minmax.max)
    print("min : ", minmax.min)

'''Time Complexity: O(n)
   Auxiliary Space: O(1) as no extra space was needed.'''


# --->> METHOD 4 -->> BY tournament method

def get_min_max(low, high, arr3):
    maxi = arr3[low]
    mini = arr3[low]

    # if there is only one element in array
    if low == high:
        maxi = arr3[low]
        mini = arr3[low]
        return(maxi, mini)

    # if 2 elements are in array
    elif high == low+1:
        if arr3[low] > arr3[high]:
            maxi = arr3[low]
            mini = arr3[high]
        else:
            maxi = arr3[high]
            mini = arr3[low]
        return (maxi, mini)
    # more than 2 elements
    else:
        mid = int((low+high)/2)
        maxi_1, mini_1 = get_min_max(low, mid, arr3)
        maxi_2, mini_2 = get_min_max(mid+1, high, arr3)
    return (max(maxi_1, maxi_2), min(mini_1, mini_2))


if __name__ == "__main__":
    n = int(input("Enter the size of array : "))
    arr3 = []
    for i in range(n):
        element = input(f'Element no. {i} --> ')
        arr3.append(element)
    high = len(arr3)-1
    low = 0
    maxi, mini = get_min_max(low, high, arr3)
    print("max : ", maxi)
    print("min : ", mini)

# --->> METHOD 5 -->> BY comparing in pairs


def miniMax(arr4,n):

     
    # If array has even number of elements then
    # initialize the first two elements as minimum
    # and maximum
    if(n % 2 == 0):
        mx = max(arr4[0], arr4[1])
        mn = min(arr4[0], arr4[1])
         
        # set the starting index for loop
        i = 2
         
    # If array has odd number of elements then
    # initialize the first element as minimum
    # and maximum
    else:
        mx = mn = arr4[0]
         
        # set the starting index for loop
        i = 1
         
    # In the while loop, pick elements in pair and
    # compare the pair with max and min so far
    while(i < n - 1):
        if arr4[i] < arr4[i + 1]:
            mx = max(mx, arr4[i + 1])
            mn = min(mn, arr4[i])
        else:
            mx = max(mx, arr4[i])
            mn = min(mn, arr4[i + 1])
             
        # Increment the index by 2 as two
        # elements are processed in loop
        i += 2
     
    return (mx, mn)
     
if __name__ == "__main__":
    n = int(input("Enter the size of array : "))
    arr4 = []
    for i in range(n):
        element = input(f'Element no. {i} --> ')
        arr4.append(element)
   
    Maxx, Minii = miniMax(arr4, n)
    print("max : ", Maxx)
    print("min : ", Minii)