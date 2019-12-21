# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None: return []
        if root.left == None and root.right == None: return [root.val]
        arr = self.pre(root,[])
        ans = []
        cou = []
        count = 2
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                while i < len(arr)-2 and arr[i+1] == arr[i+2]:
                    i += 1
                    count += 1
                if len(ans) == 0:
                    ans.append(arr[i])
                    cou.append(count)
                else:
                    if count > cou[0]:
                        ans = []
                        ans.append(arr[i])
                        cou = []
                        cou.append(count)
                    elif count == cou[0]:
                        ans.append(arr[i])
                count = 2
        if len(ans) == 0:
            return arr
        else:
            return ans

    def pre(self,root,arr):
        if root.left:
            self.pre(root.left,arr)
        arr.append(root.val)
        if root.right:
            self.pre(root.right,arr)
        return arr
