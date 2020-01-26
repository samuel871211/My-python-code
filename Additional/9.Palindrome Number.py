class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        if len(a) == 0:
            return True
        if a == a[::-1]:
            return True
        return False
