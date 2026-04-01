# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return 
        
        # 找中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 找到右半段需要翻转的起点
        second = slow.next
        # 切断左右两段的关联
        slow.next = None

        # 开始翻转右半段
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # 合并反转后的右半段和左半段
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

