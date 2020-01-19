class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        a = set()
        b = []
        for i in range(len(s)):
            for j in range(i,len(s)):
                cur = len(a)
                a.add(s[j])
                if cur == len(a):
                    b.append(cur)
                    a = set()
                    break
        return max(b)
