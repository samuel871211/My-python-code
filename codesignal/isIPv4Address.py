def isIPv4Address(a):
    b = a.split(".",4)
    if len(b) != 4:
        return False
    else:
        for i in range(len(b)):
            if str.isdigit(b[i]) == True:
                if int(b[i]) > 255 or int(b[i]) < 0:
                    return False     
            else:
                return False
        return True
