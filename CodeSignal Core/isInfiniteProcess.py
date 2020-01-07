def isInfiniteProcess(a, b):
    if a > b: return True
    if a == b: return False
    if (b-a)%2 == 0: return False
    return True
