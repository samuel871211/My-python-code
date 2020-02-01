# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        queue = [root]
        level = [0]
        arr = []
        while queue:
            node = queue.pop(0)
            curp = level.pop(0)
            if len(arr)-1 < curp:  
                arr.append([node.val])
            elif len(arr)-1 == curp:
                arr[curp].append(node.val)
            det = True
            if node.left:
                queue.append(node.left)
                level.append(curp+1)
                det = False
            if node.right:
                queue.append(node.right)
                level.append(curp+1)
        ans = []
        for i in range(len(arr)):
            ans.append(arr[i][-1])
        return ans 
