def willYou(a,b,c):
    if a and b and not c: return True
    if c and (not a or not b): return True
    return False
