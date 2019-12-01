def arrayChange(a):
    count = 0
    for i in range(len(a)-1):
        if a[i+1]<=a[i]:
            count = count + a[i] -a[i+1] + 1
            a[i+1] = a[i] + 1
    return count
