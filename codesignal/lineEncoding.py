def lineEncoding(s):
    temp = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count == 1:
                temp.append(s[i-1])
            else:
                temp.append(str(count))
                temp.append(s[i-1])
                count = 1
    if count == 1:
        temp.append(s[-1])
    else:
        temp.append(str(count))
        temp.append(s[-1])
    return "".join(temp)
