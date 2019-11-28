class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        b = []
        c = []
        if len(nums) == 1 or len(nums) == k:
            pass
        elif len(nums) < k:
            for i in range(len(nums) - k%len(nums)):
                b.append(nums[i])
            for i in range(len(nums) - k%len(nums),len(nums)):
                c.append(nums[i])
            for i in range(len(c)):
                nums[i] = c[i]
            for i in range(len(b)):
                nums[i+len(c)] = b[i]
        else:
            for i in range(len(nums)-k):
                b.append(nums[i])
            for i in range(len(nums)-k,len(nums)):
                c.append(nums[i])
            for i in range(len(c)):
                nums[i] = c[i]
            for i in range(len(b)):
                nums[i+len(c)] = b[i]
