# Takes an array of integers and returns an array containing (all) the positions of the largest integer in the array

def biggestInPositions(arrayOfNumbers, arrayOfIndexes = [], biggestNumberInWholeList=0, index=0):
    if len(arrayOfNumbers)==0:
        for i in range(len(arrayOfIndexes)):
            arrayOfIndexes[i] = arrayOfIndexes[i] - 1
        return arrayOfIndexes
    else:
        biggestNumber = biggestNumberInWholeList
        biggestNumberInCurrentList = biggestIn(arrayOfNumbers)
        if(biggestNumberInCurrentList >= biggestNumber):
            biggestNumber = biggestNumberInCurrentList
        else:
            for i in range(len(arrayOfIndexes)):
                arrayOfIndexes[i] = arrayOfIndexes[i] - 1
            return arrayOfIndexes
        index = biggestInPos(arrayOfNumbers) + 1
        if(arrayOfIndexes != []):
            indexInOriginal = arrayOfIndexes[len(arrayOfIndexes)-1] + index
            arrayOfIndexes.append(indexInOriginal)
        else:
            arrayOfIndexes.append(index)
        del arrayOfNumbers[:index]

        return biggestInPositions(arrayOfNumbers, arrayOfIndexes, biggestNumber, index)
    
print(biggestInPositions([5,12,31,7,25,31,18,7,31]))
