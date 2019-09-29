def getSum(piece):
    if len(piece) == 0:
        return 0
    else:
        return piece[0] + getSum(piece[1:])


def question6(f, x, y, z):
    xSum = f(x)
    ySum = f(y)
    zSum = f(z)

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


question6(getSum, [1, 2, 3], [10, 20, 30, 40], [65, 32, 3])
