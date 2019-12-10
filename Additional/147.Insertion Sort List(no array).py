# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            new = ListNode(head.val)
            compare_node = head.next
            current_node = new
            current_next = new.next
            while compare_node != None:
                if compare_node.val <= current_node.val:
                    newhead = ListNode(compare_node.val)
                    newhead.next = new
                    new = newhead
                else:
                    while current_next != None and current_next.val < compare_node.val:
                        current_node = current_next
                        current_next = current_next.next
                    if current_next == None:
                        current_node.next = ListNode(compare_node.val)
                    else:
                        new_insert = ListNode(compare_node.val)
                        current_node.next = new_insert
                        new_insert.next = current_next
                compare_node = compare_node.next
                current_node = new
                current_next = new.next
            return new
