class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = sorted(nums1+nums2)
        if len(ans)%2 == 1:
            return ans[len(ans)//2]
        else:
            return (ans[len(ans)//2] + ans[len(ans)//2 - 1])/2
