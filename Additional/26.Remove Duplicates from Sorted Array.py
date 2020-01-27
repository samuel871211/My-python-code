class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            while nums[i] == nums[i+1]:
                nums.pop(i)
                if i+1 == len(nums):
                    break
            i += 1
        return len(nums)
