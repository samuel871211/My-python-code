def commonCharacterCount(s1, s2):
    count = 0
    for i in set(s1):
        if i in s2:
            count = count + min(s1.count(i),s2.count(i))
    return count
