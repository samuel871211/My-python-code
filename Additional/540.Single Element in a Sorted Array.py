class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) == 1:
                return i
