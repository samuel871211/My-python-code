# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root:
            arr = self.traversal(root,[])
            ans = abs(arr[1] - arr[0])
            for i in range(1,len(arr)-1):
                cur = abs(arr[i+1] - arr[i])
                if cur < ans:
                    ans = cur
            return ans    
        
    def traversal(self,root,arr):
        if root.left:
            self.traversal(root.left,arr)
        arr.append(root.val)
        if root.right:
            self.traversal(root.right,arr)
        return arr
