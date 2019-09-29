def question4(x, y, z):
    if len(x) == len(y) == len(z):
        print("All three inputs have equal lengths")
    elif len(x) == len(y):
        print("x and y have equal lengths")
    elif len(x) == len(z):
        print("x and z have equal lengths")
    elif len(y) == len(z):
        print("y and z have equal lengths")
    else:
        print("All the three inputs have different lengths")


question4([1, 2, 3], [10, 20, 30, 40], [65, 32, 7])
