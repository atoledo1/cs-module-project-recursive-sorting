# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
   
    if (len(arr) == 0):
        return -1
    if start > end:
        return - 1
    else:
        mid = start + end // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, (mid - 1))
        else:
            return binary_search(arr, target, (mid+1), end)
