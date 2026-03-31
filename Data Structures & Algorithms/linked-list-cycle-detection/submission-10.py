class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # 只要 fast 和 fast.next 都存在，就可以安全地往前跳两步
        while fast and fast.next:
            slow = slow.next            # 慢指针走一步
            fast = fast.next.next       # 快指针走两步
            
            if slow == fast:            # 两人相遇，有环
                return True
                
        # 循环自然结束，说明 fast 走到了尽头（遇到 None），没有环
        return False