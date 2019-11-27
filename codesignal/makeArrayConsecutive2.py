def makeArrayConsecutive2(statues):
    a = sorted(statues)
    return a[-1]-a[0]+1-len(a)
