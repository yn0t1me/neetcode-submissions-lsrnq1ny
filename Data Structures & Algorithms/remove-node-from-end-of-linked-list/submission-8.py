# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 让slow和fast指针隔开合适的距离
        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        # 让fast走到尾节点，slow恰好在目标节点的前一个节点
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
        
        
