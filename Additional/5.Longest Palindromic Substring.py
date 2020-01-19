class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        ans = None
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if s[i] == s[j]:
                    if s[i:j+1] == s[i:j+1][::-1]:
                        if not ans:
                            ans = s[i:j+1]
                        elif (j-i) >= len(ans): 
                            ans = s[i:j+1]
        if not ans:
            return s[0]
        return ans
