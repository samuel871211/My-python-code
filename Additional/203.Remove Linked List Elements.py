# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None          
        elif head.val == val:
            head = head.next
            if head == None:
                return None
            else:
                return Solution().removeElements(head,val)
        else:
            cur = head
            while cur.next != None and cur.next.val != val:
                cur = cur.next
            if cur.next == None:
                return head
            else:
                cur.next = cur.next.next
                if cur.next == None:
                    return head
                else:
                    return Solution().removeElements(head,val)
