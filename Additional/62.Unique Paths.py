class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top = m+n-2
        topval = 1
        bottom = 1
        for i in range(1,n):
            bottom = bottom*i
            topval = topval*top
            top = top-1
        return topval//bottom
