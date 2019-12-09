# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return None
        else:
            if root.val == val:
                return root
            elif root.val < val:
                return Solution().searchBST(root.right,val)
            else:
                return Solution().searchBST(root.left,val)
