# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            arr = []
            for i in range(len(lists)):
                cur = lists[i]
                while cur != None:
                    arr.append(cur.val)
                    cur = cur.next
            arr = sorted(arr)
            if len(arr) == 0:
                return None
            else:
                head = ListNode(arr[0])
                cur = head
                for i in range(1,len(arr)):
                    cur.next = ListNode(arr[i])
                    cur = cur.next
                return head
