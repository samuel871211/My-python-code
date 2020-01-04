def electionsWinners(a,k):
    a = sorted(a)
    for i in range(len(a)):
        if a[i] + k > a[-1]:
            return len(a)-i
    if a[-1] > a[-2]:
        return 1
    return 0
