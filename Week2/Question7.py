# Takes two arrays of integers in accending order and returns the number of integers that occur in both arrays

def isIn(B, k):
       for i in range(len(B)):
            if B[i] > k:
                return False
            if B[i] == k:
                return True

def occurInBothEfficient(A, B):
    counter = 0
    for i in range(len(A)):
        if(isIn(B,A[i])):
            counter = counter + 1
    return counter

print(occurInBothEfficient([5,7,12,25,31], [4,7,8,12,31,42]))