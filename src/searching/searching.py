# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
   if start > end: # check if list is sorted ascending.
        return -1
   mid = start + end //2 # get middle floor
   if target == arr[mid]:
       return mid
   elif target < arr[mid]:
        return binary_search(arr, target, start, mid -1)
   else:
        return binary_search(arr, target, mid +1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    start = 0 #arr[0]
    end = len(arr) #arr[len(arr) - 1]
    mid = start + end // 2 # get middle floor
    if arr[start] < arr[end -1]: # check if list is sorted ascending.
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:# remove right side (larger numbers)
            end = mid - 1
            return agnostic_binary_search(arr, target)
        else:# remove left side (smaller numbers)
            start = mid + 1
            return agnostic_binary_search(arr, target)
    else:
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:# remove left side (larger numbers)
            start = mid + 1
            return agnostic_binary_search(arr, target)
        else:# remove right side (smaller numbers)
            end = mid - 1
            return agnostic_binary_search(arr, target)



