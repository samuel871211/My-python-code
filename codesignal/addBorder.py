def addBorder(a):
    b = [None]*(len(a))
    c = len(a[0])+2
    for i in range(len(a)):
        a.insert(3*i,"*")
        a.insert(3*i+2,"*")
    for i in range(len(b)):
        s = "".join(a[:3])
        b[i] = s
        a = a[3:]
    b.insert(0,"*"*c)
    b.append("*"*c)
    return b
