def question3():
    x = input("Give an x value: ")
    y = input("Give a y value: ")
    z = input("Give an z value: ")
    if x == y == z:
        print("All three inputs have equal values")
    elif x == y:
        print("x and y have equal values")
    elif x == z:
        print("x and z have equal values")
    elif y == y:
        print("y and z have equal values")
    else:
        print("All the three inputs have different values")


question3()
