import random

def randomIntArray(s, n):
    randomArray = [None] * s
    for i in range(s):
        randomArray[i] = random.randint(0, n)
    
    return randomArray

print(randomIntArray(100,5))