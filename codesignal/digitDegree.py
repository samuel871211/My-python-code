def digitDegree(n):
    return helper(n,0,0)

def helper(n,count,temp):
    a = str(n)
    if len(a) == 1:
        return count
    else:
        for i in range(len(a)):
            temp += int(a[i])
        count += 1
        if temp < 10:
            return count
        else:
            n = temp
            return helper(n,count,0)
