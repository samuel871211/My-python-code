def sumUpNumbers(a):
    final = []
    temp = []
    for i in range(len(a)):
        if a[i].isdigit():
            temp.append(a[i])
        else:
            if temp:
                final.append(int("".join(temp)))
            temp = []
    if temp:
        final.append(int("".join(temp)))
    return sum(final) 
