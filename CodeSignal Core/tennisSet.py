def tennisSet(a,b):
    if (a==7 and (b==6 or b==5)) or (b==7 and (a==6 or a==5)): return True
    if (a==6 and b<=4) or (b==6 and a<=4): return True
    return False
