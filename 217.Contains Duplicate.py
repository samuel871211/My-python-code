class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            cur = len(s)
            s.add(nums[i])
            if len(s) == cur:
                return True
        return False
