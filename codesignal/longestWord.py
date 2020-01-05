def longestWord(a):
    temp = []
    ans = None
    for i in range(len(a)):
        if a[i].isalpha():
            temp.append(a[i])
        else:
            if temp:
                if not ans or len(temp) > len(ans):
                    ans = "".join(temp)
            temp = []
    if temp:
        if not ans or len(temp) > len(ans):
            ans = "".join(temp)
    return ans
