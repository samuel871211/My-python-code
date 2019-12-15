class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == len(nums2)-1 or max(nums2[j+1:]) <= nums2[j]:
                        ans.append(-1)
                    else:
                        for k in range(j+1,len(nums2)):
                            if nums2[j] < nums2[k]:
                                ans.append(nums2[k])
                                break
        return ans    
