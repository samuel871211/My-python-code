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
            curp = head
            cur = head.next
            if curp.val == cur.val:              
                while cur.next != None and cur.next.val == cur.val:
                    cur = cur.next
                head = cur.next
                return self.deleteDuplicates(head)
            else:
                while cur.next != None and cur.next.val != cur.val:
                    curp = cur
                    cur = cur.next
                if cur.next == None:
                    return head
                else:
                    while cur.next != None and cur.next.val == cur.val:
                        cur = cur.next
                    curp.next = cur.next
                    return self.deleteDuplicates(head)
