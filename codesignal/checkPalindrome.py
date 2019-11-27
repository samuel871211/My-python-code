def checkPalindrome(inputString):
    a = []
    for i in inputString:
        a.append(i)
    if a == a[::-1]:
        return True
    else:
        return False
