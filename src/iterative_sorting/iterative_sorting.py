# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # TO-DO: swap
        # Your code here

        # loop from the current index to the end of the array
        for j in range(cur_index + 1, len(arr)):
                # find the smallest value in the array: 'j'
                if arr[j] < arr[smallest_index]:
                    smallest_index = j
        # swap the smallest value to your 'cur_index'
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # capture a variable for len() of the array
    size = len(arr)

    # loop through the full array but not the outer loop (-1)
    for i in range(size-1):
        # traverse array from the start (0)
        # until the values we haven't sorted before (-i)
        # and also not the outer loop (-1)
        for j in range(0, size-i-1):
            # compare each value to it's next, and when it is greater
            if arr[j] > arr[j+1]:
                # swap the values
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # return the array
    return arr

test_arr = [25, 65, 100, 15, 35, 20, 10] 

bubble_sort(test_arr)

# command line formatting
print ("Sorted array is:") 
for i in range(len(test_arr)): 
    print (f"{test_arr[i]}")

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# overall runtime: O(n + m)
# space complexity: O(n + m)
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr

    if maximum is None:
        maximum = max(arr)
    
    buckets = [0 for i in range(maximum+1)]

    # loop through our arr
    # O(n) since we're running through every element in the input array
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort!"
        # for each distinct arr value, increment arr[value] by 1
        buckets[value] += 1

    # at this point, our buckets array has all of the counts of
    # every distinct value in our input array

    output = []
    # loop through our buckets array
    # length of buckets can be at most 0..m where m is our m possible value
    for index, count in enumerate(buckets):
        # for the current count
        output.extend([index for i in range(count)])
        # add that many values to an output array

    return output
