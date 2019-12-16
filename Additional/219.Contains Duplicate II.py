class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # ind = 0
        # pos = []
        # same = []
        # while ind < len(nums):
        #     if nums[ind] not in same and nums.count(nums[ind]) > 1:
        #         same.append(nums[ind])
        #         for i in range(ind,len(nums)):
        #             if nums[i] == nums[ind]:
        #                 pos.append(i)
        #                 if len(pos) >= 2:
        #                     if abs(pos[-1] - pos[-2]) <= k:
        #                         return True
        #             if len(pos) == nums.count(nums[ind]):
        #                 break
        #     pos = []
        #     ind += 1
        # return False
        
        # cur_index = []
        # j = 0
        # count = 0
        # a = list(set(nums))
        # for i in range(len(a)):
        #     b = nums.count(a[i])
        #     if b > 1:
        #         while count < b:
        #             if a[i] == nums[j]:
        #                 cur_index.append(j)
        #                 count += 1
        #             if len(cur_index) > 1:
        #                 if abs(cur_index[-1] - cur_index[-2]) <= k:
        #                     return True
        #                 else:
        #                     cur_index.pop(0)
        #             j += 1
        #         cur_index = []
        #         count = 0
        #         j = 0
        # return False
        temp = set()
        for i in range(len(nums)):
            if i > k:
                temp.remove(nums[i-k-1])
            if nums[i] in temp:
                return True
            temp.add(nums[i])
        return False 
