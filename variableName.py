def variableName(a):
    if a[0].isalpha() == True or a[0] == "_":
        for i in range(1,len(a)):
            if a[i].isdigit() == False and a[i].isalpha() == False and a[i] != "_":
                return False
        return True
    return False
