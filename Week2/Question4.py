# Takes an array of integers and returns the index of the biggest integer in the array

def biggestInPos(A):
    biggest = biggestIn(A)
    return A.index(biggest)
    
print(biggestInPos([5,12,31,7,25]))
