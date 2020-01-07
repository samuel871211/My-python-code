def lateRide(n):
    hour = str(n//60)
    minute = str(n-(60*(n//60)))
    final = 0
    for i in range(len(hour)):
        final += int(hour[i])
    for i in range(len(minute)):
        final += int(minute[i])
    return final
