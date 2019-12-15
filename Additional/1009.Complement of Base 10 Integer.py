a = bin(a)
        a = a[2:]
        a = list(a)
        for i in range(len(a)):
            if a[i] == str(0):
                a[i] = "1"
            else:
                a[i] = "0"
        a = "".join(a)
        a = int(a,2)
        return a
