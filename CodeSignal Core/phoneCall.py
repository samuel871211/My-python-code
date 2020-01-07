def phoneCall(a,b,c,d):
    count = 0
    if d < a: return count
    if d == a: return count+1
    d = d-a
    count += 1
    det = False
    while d-b >= 0:
        d = d-b
        count += 1
        if count == 10:
            det = True
            break
    if not det:
        return count
    if det:
        while d-c >= 0:
            d = d-c
            count += 1
        return count
