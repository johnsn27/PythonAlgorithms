# Takes two arrays of integers and returns the number of integers that occur in both arrays

def isIn(B, k):
       for i in range(len(B)):
            if B[i] == k:
                return True

def occurInBoth(A, B):
    counter = 0
    for i in range(len(A)):
        if(isIn(B,A[i])):
            counter = counter + 1
    return counter

print(occurInBoth([5,12,31,7,25], [4,12,8,7,42,31]))
