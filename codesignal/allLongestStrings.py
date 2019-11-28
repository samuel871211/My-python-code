def allLongestStrings(inputArray):
    b = []
    c = []
    for i in inputArray:
        b.append(len(i))
    print(b)
    for i in range(len(b)):
        if b[i] == max(b):
            c.append(inputArray[i])
    return c
