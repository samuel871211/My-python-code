def deleteDigit(n):
    n = str(n)
    temp = []
    for i in range(len(n)):
        temp.append(n[i])
    a = temp.pop(0)
    pivot = int("".join(temp))
    temp.insert(0,a)
    compare = 0
    for i in range(1,len(n)):
        b = temp.pop(i)
        compare = int("".join(temp))
        if compare > pivot:
            pivot = compare
        temp.insert(i,b)
        compare = 0
    return pivot
