# Takes an array of integers and returns the index of the biggest integer in the array

from Week2.Question3 import biggestIn

def biggestInPos(A):
    biggest = biggestIn(A)
    return A.index(biggest)
    
print(biggestInPos([5,12,31,7,25]))
