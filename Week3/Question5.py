import time
from Week3.Question2 import randomIntArray


def insertionSort(A):
    for i in range(1, len(A)):
        insert(A[i], A, i)


def insert(k, A, hi):
    for i in range(hi-1, -1, -1):
        if k >= A[i]:
            A[i+1] = k
            return
        A[i+1] = A[i]
    A[0] = k


def sortTimeUsing(sortf, A):
    t = time.time()
    insertionSort(A)
    t = time.time()-t
    return t


arrayToSort1 = randomIntArray(0, 5)
arrayToSort2 = randomIntArray(1000, 5)
sortedArray2 = sortTimeUsing(arrayToSort2)
arrayToSort3 = randomIntArray(100000, 5)
print(sortTimeUsing(insertionSort, arrayToSort1))
print(sortTimeUsing(insertionSort, sortedArray2))
print(sortTimeUsing(insertionSort, arrayToSort3))
