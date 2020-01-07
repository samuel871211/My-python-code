class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [0]*len(nums)
        arr[0] = nums[0]
        cur = nums[0]
        for i in range(1,len(nums)):
            arr[i] = max(nums[i],nums[i]+arr[i-1])
            cur = max(cur,arr[i])
        return cur
