class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        nums = sorted(nums)
        k = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                if nums[i] == k:
                    k += 1
                else:
                    if i == 0:
                        return k
                    elif nums[i] != nums[i-1]:
                        return k
        return k
