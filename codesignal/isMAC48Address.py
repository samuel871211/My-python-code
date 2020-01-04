def isMAC48Address(a):
    a = a.split("-")
    print(a)
    if len(a) != 6:
        return False
    for i in range(len(a)):
        if len(a[i]) != 2:
            return False
        if a[i][0].isdigit() == False and a[i][0] != "A" and a[i][0] != "B" and a[i][0] != "C" and a[i][0] != "D" and a[i][0] != "E" and a[i][0] != "F":
            return False
        if a[i][1].isdigit() == False and a[i][1] != "A" and a[i][1] != "B" and a[i][1] != "C" and a[i][1] != "D" and a[i][1] != "E" and a[i][1] != "F":
            return False
    return True
