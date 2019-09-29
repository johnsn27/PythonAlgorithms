# Takes an array of integers and an integer as inputs and multiplies every integer in the array by the integer argument.

def multAll(A, k):
    return [i * k for i in A]

print(multAll([5,12,31,7,25], 10))