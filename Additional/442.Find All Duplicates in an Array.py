class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        ans = []
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                ans.append(a[i])
        return ans
