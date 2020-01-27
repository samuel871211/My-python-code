# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []
        cur = head
        while cur != None:
            arr.append(cur)
            cur = cur.next
        if n == 1:
            if len(arr) == 1:
                return None
            else:
                arr[-2].next = None
                return head
        if n == len(arr):
            return arr[-n+1]
        arr[-n-1].next = arr[-n+1]
        return head
