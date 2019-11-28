def isLucky(n):
    a = []
    for i in str(n):
        a.append(i)
    b = 0
    for i in range(len(a)//2):
        b = b + int(a[i])
    c = 0
    for i in range(len(a)//2,len(a)):
        c = c + int(a[i])
    if b == c:
        return True
    else:
        return False
