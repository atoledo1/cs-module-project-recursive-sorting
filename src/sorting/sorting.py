# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0
    for i in range(0, elements):

        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b = b + 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a = a + 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a = a + 1
        else:
            merged_arr[i] = arrB[b]
            b = b + 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):

    if len(arr) > 1:
        middle = len(arr)//2
        arrLeft = arr[:middle]
        arrRight = arr[middle:]

        left = merge_sort(arrLeft)
        right = merge_sort(arrRight)
        arr = merge(left, right)

    return arr

