def partition(arr):
    # pick a pivot
    pivot = arr[0]
    left = []
    right = []

    # partition the elements around the pivot
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    return left, pivot, right

def quicksort(arr):
    # base case; if length of the array is <= 1
    if len(arr) <= 1:
        return arr
    
    # otherwise, we need to call our partition function to break the input
    # array into amaller chunks
    left, pivot, right = partition(arr)

    # pivot needs to be type: list
    pivot = [pivot]
    
    # run quicksort recursively on the left and right partitions to break them
    # down further into smaller pieces
    qleft = quicksort(left)
    qright = quicksort(right)

    # concatenate all the pieces together
    return qleft + pivot + qright

arr = [13, 17, 5, 18, 27, 22, 16, 3]
arr = quicksort(arr)
print(arr)