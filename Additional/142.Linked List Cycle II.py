# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        a = [head]
        while head.next != None and head.next not in a:
            a.append(head.next)
            head = head.next
        if head.next == None:
            return None
        else:
            return head.next
