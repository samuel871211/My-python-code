def findEmailDomain(a):
    det = False
    for i in range(len(a)):
        if a[i] == "@":
            det = True
            a = a[i+1:]
            break
    if det:
        return findEmailDomain(a)
    else:
        return a
