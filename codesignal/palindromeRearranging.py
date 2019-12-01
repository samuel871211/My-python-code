def palindromeRearranging(a):
    count = 0
    for i in set(a):
        if a.count(i)%2 != 0:
            count += 1
        if count >=2:
            return False
    return True
