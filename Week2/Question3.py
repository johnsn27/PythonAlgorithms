# Takes an array of integers and returns the biggest integer in the array.

def biggestIn(A):
    max= 0
    for i in A:
        if i > max:
            max=i
    return max

print(biggestIn([5,12,31,7,25]))