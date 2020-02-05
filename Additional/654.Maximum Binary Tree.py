# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if not nums: return None

        root = TreeNode(max(nums))
        return self.helper(nums,root)
    
    def helper(self,nums,root):
        
        pivot = nums.index(max(nums))
        left , right = nums[:pivot] , nums[pivot+1:]
        
        if left:
            root.left = TreeNode(max(left))
            self.helper(left,root.left)
        
        if right:
            root.right = TreeNode(max(right))
            self.helper(right,root.right) 
        
        return root
