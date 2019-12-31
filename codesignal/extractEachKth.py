def extractEachKth(a,k):
    for i in range(1,len(a)//k+1):
        a.pop(i*k-1*(i-1)-1)
    return a
