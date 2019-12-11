# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        arr = Solution().pre(root,[])
        arr = sorted(arr)
        ans = 0
        for i in range(len(arr)):
            if arr[i] >= L and arr[i] <= R:
                ans = ans + arr[i]
            if arr[i] == R:
                break
        return ans         
    
    def pre(self,root,arr):
        if root == None:
            return arr
        else:
            arr.append(root.val)
            if root.left is not None:
                Solution().pre(root.left,arr)
            if root.right is not None:
                Solution().pre(root.right,arr)
            return arr
