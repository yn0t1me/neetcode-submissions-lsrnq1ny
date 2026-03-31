# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        c = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                c.next = list1
                c = c.next
                list1 = list1.next
            else:
                c.next = list2
                c = c.next
                list2 = list2.next
        c.next = list1 if list1 else list2
        return new_head.next
