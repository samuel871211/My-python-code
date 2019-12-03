class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        elif n == 0:
            pass
        else:
            m -= 1
            n -= 1
            i = -1
            while m >= 0 and n >= 0:
                if nums1[m] >= nums2[n]:
                    nums1[i] = nums1[m]
                    m -= 1
                    i -= 1
                elif nums1[m] < nums2[n]:
                    nums1[i] = nums2[n]
                    n -= 1
                    i -= 1
            while m < 0 and n >= 0:
                nums1[i] = nums2[n]
                n -= 1
                i -= 1
