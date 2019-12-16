class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # a = list(set(nums))
        # for i in range(len(a)):
        #     if nums.count(a[i]) > 1:
        #         return a[i]
        a = sorted(nums)
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                return a[i]
