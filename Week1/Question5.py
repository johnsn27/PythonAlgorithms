def getSum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + getSum(array[1:])


def question5(x, y, z):
    xSum = getSum(x)
    ySum = getSum(y)
    zSum = getSum(z)

    if xSum == ySum == zSum:
        print("All three inputs have equal values")
    elif xSum == ySum:
        print("x and y have equal values")
    elif xSum == zSum:
        print("x and z have equal values")
    elif ySum == zSum:
        print("y and z have equal values")
    else:
        print("All the three inputs have different values")


question5([1, 2, 3], [10, 20, 30, 40], [65, 32, 3])
