import random


def selectionSort(A):
    for i in range(len(A)):
        imin = findMin(i, A)
        swap(i, imin, A)


def findMin(i, A):
    imin = i
    for j in range(i+1, len(A)):
        if A[j] < A[imin]:
            imin = j
    return imin


def swap(i, j, A):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


def sortTime(A):
    t = time.time()
    selectionSort(A)
    t = time.time()-t


print(sortTime(100, 5))
