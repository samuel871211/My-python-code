class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A == sorted(A):
            return True
        elif A[::-1] == sorted(A):
            return True
        else:
            return False
