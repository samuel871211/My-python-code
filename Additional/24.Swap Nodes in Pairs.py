# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            cur = head
            self.helper(cur)
            return head
   
    def helper(self,cur):
        if cur.next:
            cur.val,cur.next.val = cur.next.val,cur.val
            if cur.next.next:
                self.helper(cur.next.next)
