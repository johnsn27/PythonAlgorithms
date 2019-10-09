def insertionSort(A, counter=[]):
    for i in range(1,len(A)):
        insert(A[i],A,i, counter)
    return A, len(counter)
def insert(k, A, hi, counter):
    for i in range(hi-1,-1,-1):
        counter.append(1)
        if k >= A[i]:
            A[i+1] = k
            return
        A[i+1] = A[i]
    A[0] = k
    
print(insertionSort([1,2,3,4,5,6,7,8,9,10]))