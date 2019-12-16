# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            curp, cur = head, head.next
            
            if curp.val == cur.val:
                while cur != None and curp.val == cur.val:
                    cur = cur.next
                curp.next = cur
            else:
                while cur != None and curp.val != cur.val:
                    curp = cur
                    cur = cur.next
                if cur == None:
                    return head
                else:
                    while cur != None and curp.val == cur.val:
                        cur = cur.next
                    curp.next = cur
            return self.deleteDuplicates(head)
