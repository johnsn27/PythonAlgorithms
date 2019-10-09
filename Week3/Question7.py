def insertionSortRecursive(arr, arrayLength = len(arr)):
    # base case
    if arrayLength <= 1:
        return arr

    # Sort first n-1 elements
    insertionSortRecursive(arr, arrayLength-1)
    # Insert last element at its correct position in sorted array.
    last = arr[arrayLength-1]
    j = arrayLength-2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while (j >= 0 and arr[j] > last):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = last
    return arr

# Driver program to test insertion sort
# arr = [12, 11, 13, 5, 6]
# n = len(arr)
# print(insertionSortRecursive(arr, n))

# arr = [2,4,6,8,10,1,3,5,7,9]
# n = len(arr)

print(insertionSortRecursive([1,2,3,4,5,6,7,8,9,10]))
print(insertionSortRecursive([1,2,3,4,5,6,7,8,9,10]))
print(insertionSortRecursive([10,9,8,7,6,5,4,3,2,1]))