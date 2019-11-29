def sortByHeight(a):
    b = []
    c = []
    for i in a:
        if i != -1:
            b.append(i)
    sor = sorted(b)
    for i in range(len(a)):
        if a[i] != -1:
            c.append(i)
    for i in range(len(b)):
        a[c[i]] = sor[i]
    return a
