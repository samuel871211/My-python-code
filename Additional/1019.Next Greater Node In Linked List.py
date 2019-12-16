# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        lst = [] #紀錄linked list的value
        tem = [] #從tail開始往head走，紀錄當前的最大值
        while head != None:
            lst.append(head.val)
            head = head.next
        for i in range(len(lst)-1,-1,-1):
            while tem and tem[-1] <= lst[i]:
                tem.pop()
            tem.append(lst[i])
            if len(tem) > 1:
                lst[i] = tem[-2]
            else:
                lst[i] = 0
        return lst
