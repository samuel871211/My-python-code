def arrayMaximalAdjacentDifference(a):
    diff = []
    for i in range(len(a)-1):
        diff.append(abs(a[i]-a[i+1]))
    return max(diff)
