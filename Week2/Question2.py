# Takes an array of integers and an integer as inputs and multiplies every integer in the array by the integer argument.
# Immutatble 

def multAll2(A, k):
    newA = [i * k for i in A]
    return newA

print(multAll2([5,12,31,7,25], 10))