def longestDigitsPrefix(a):
    if a[0].isdigit():
        count = 1
        while a[count].isdigit() and count < len(a):
            count += 1
            if count == len(a):
                break
        return a[0:count]
    return ""
