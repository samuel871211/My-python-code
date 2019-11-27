def adjacentElementsProduct(inputArray):
    cur = []
    for i in range(len(inputArray)-1):
        cur.append(inputArray[i]*inputArray[i+1])
    cur = sorted(cur)
    return cur[-1]
