def buildPalindrome(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return s+s[:i][::-1]
