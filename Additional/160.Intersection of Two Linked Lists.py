# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA== None or headB==None:
            return None
        detA,detB=True,True
        curA,curB=headA,headB
        while curA!=curB:
            if detA and curA.next==None:
                curA=headB
                detA=False
            else:
                curA=curA.next
            
            if detB and curB.next==None:
                curB=headA
                detB=False
            else:
                curB=curB.next
        return curA
#(a1>a2>c1>c2>c3)>(b1>b2>b3)>c1
#(b1>b2>b3>c1>c2>c3)>(a1>a2)>c1
