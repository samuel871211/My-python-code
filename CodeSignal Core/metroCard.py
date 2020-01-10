def metroCard(k):
    a = [31,28,31,30,31,30,31,31,30,31,30,31]
    b = []
    for i in range(1,12):
        if a[i] == k:
            if a[i-1] not in b:
                b.append(a[i-1])
    return b
