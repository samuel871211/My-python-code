class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            count = nums.count(i)
            if count > 2:
                for j in range(count-2):
                    nums.remove(i)
