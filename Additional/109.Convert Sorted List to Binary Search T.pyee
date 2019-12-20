# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None: return None
        if head.next == None: return TreeNode(head.val)
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.helper(arr)
    
    def helper(self,arr):
        if len(arr) > 0:
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = self.helper(arr[:mid])
            root.right = self.helper(arr[mid+1:])
            return root 
