# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        else:
            if head.next == head:
                return True
            else:
                a = []
                a.append(head)
                head = head.next
                while head != None and head not in a:
                    a.append(head)
                    head = head.next
                if head == None:
                    return False
                else:
                    return True
