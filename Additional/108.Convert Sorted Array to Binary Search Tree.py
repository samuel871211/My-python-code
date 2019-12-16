# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.helper(nums,0,len(nums)-1)
    
    def helper(self,nums,head,tail):
        if head > tail:
            return None
        else:
            mid = (head + tail)//2
            root = TreeNode(nums[mid])
            root.left = self.helper(nums,head,mid-1)
            root.right = self.helper(nums,mid+1,tail)
        return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return None
        mid = len(nums)//2
        new = TreeNode(nums[mid])
        new.left = self.sortedArrayToBST(nums[:mid])
        new.right = self.sortedArrayToBST(nums[mid+1:])
        return new
