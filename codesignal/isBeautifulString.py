def isBeautifulString(a):
    import string
    a = sorted(a)
    b = string.ascii_lowercase
    print("a=",a)
    print("b=",b)
    index = 0
    count = 0
    prev = 0
    if a[0] != "a":
        return False
    else:
        count += 1
    for i in range(1,len(a)):
        if index < 25 and a[i] == b[index+1]:
            if prev == 0 or count <= prev:
                prev = count   
            else:
                return False
            count = 1
            index += 1   
        elif a[i] == b[index]:
            count += 1
        else:
            return False
    if prev != 0 and count > prev:
        return False
    return True
