# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, a: ListNode, b: ListNode) -> ListNode:
        aa , bb = [] , []
        while a:
            aa.append(str(a.val))
            a = a.next
        while b:
            bb.append(str(b.val))
            b = b.next
        c = "".join(aa[::-1])
        d = "".join(bb[::-1])
        e = int(c) + int(d)
        e = str(e)
        e = e[::-1]
        head = ListNode(int(e[0]))
        cur = head
        for i in range(1,len(e)):
            cur.next = ListNode(int(e[i]))
            cur = cur.next
        return head
