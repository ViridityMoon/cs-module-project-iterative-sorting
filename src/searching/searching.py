"""
Takes in a/n array/list and a target value and returns the index of the target if it
is there. If it is not contained, it will return -1, an invalid index.
"""
def linear_search(arr, target):
    # loop through every index
    for i in range(len(arr)):
        cur_index = i
        # if the value of 'cur_index' is the target, return the index
        if arr[cur_index] == target:
            return cur_index
    # if we reach here, we never found the value (worst case)
    return -1   # not found


# Write an iterative implementation of Binary Search
"""
Takes in a sorted array/list and a target value and returns the index of the target if it
is there. If it is not contained, it will return -1, an invalid index.
"""
def binary_search(arr, target):
    # Your code here
    # define variables for the beginning of the array
    # and the end of the array
    left = 0
    right = len(arr) - 1

    # while the left variable and right variable are 
    # different
    while left <= right:
        # define a midpoint between the right and left
        midpoint = (right + left) // 2

        # if the midpoint is the target; return it
        if arr[midpoint] == target:
            return midpoint
        # if the midpoint is less, decrement the right variable
        elif arr[midpoint] > target:
            right = midpoint - 1
        # if the midpoint is greater, increment the left variable
        else:
            left = midpoint + 1
    # if we reach here, we never found the value (worst case)
    return -1  # not found

test_list = [10, 28, 32, 36, 55]

print(binary_search(test_list, 10))