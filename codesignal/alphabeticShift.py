def alphabeticShift(a):
    import string
    b = string.ascii_lowercase
    b = b+"a"
    print(b)
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(b[j+1])
                break
    print(c)
    d = "".join(c)
    return d
