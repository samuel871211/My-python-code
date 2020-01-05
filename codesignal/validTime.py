def validTime(time):
    if -1 < int(time[:2]) < 24 and -1 < int(time[3:]) < 60: return True
    return False
