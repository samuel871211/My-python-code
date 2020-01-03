def growingPlant(a,b,c):
    total = 0
    count = 0
    while True:
        total += a
        count += 1
        if total >= c:
            return count
        total -= b
