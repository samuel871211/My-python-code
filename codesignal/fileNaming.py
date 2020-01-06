def fileNaming(a):
    return helper(a,[],)
def helper(a,b):
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
        else:
            count = 1
            temp = a[i]
            a[i] = a[i] +"("+str(count)+")"
            while a[i] in b:
                count += 1
                a[i] = temp
                a[i] = a[i] +"("+str(count)+")"
            b.append(a[i])
    return b
