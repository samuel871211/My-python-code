class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        if len(a) == 0:
            return None
        else:
            a.reverse()
            newhead = ListNode(a[0])
            cur = newhead
            for i in range(1,len(a)):
                cur.next = ListNode(a[i])
                cur = cur.next
            return newhead
