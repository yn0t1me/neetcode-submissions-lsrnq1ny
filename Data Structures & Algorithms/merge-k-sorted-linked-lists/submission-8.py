# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 边界防御：如果根本没有链表，直接返回 None
        if not lists:
            return None
        
        # 只要列表中还有超过 1 个链表，就说明还没合并完
        while len(lists) > 1:
            # 每一轮合并，都需要一个全新的临时列表来装新生成的链表
            temp_l =[]
            
            # 步长为 2，两两一对进行遍历
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                
                # 防御性获取 list2：如果 i+1 没有越界，说明能凑成一对；否则说明是落单的
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                if list2:
                    # 如果能凑成一对，合并它俩，并放进下一轮的名单中
                    temp_l.append(self.merge2Lists(list1, list2))
                else:
                    # 如果落单了（奇数个链表的最后一步），直接原封不动放进下一轮
                    temp_l.append(list1)
            
            # 把本轮合并后的新链表集合，覆盖掉旧的 lists，进入下一轮
            lists = temp_l
            
        # 当 lists 里只剩 1 个元素时，大功告成
        return lists[0]


    def merge2Lists(self,list1, list2):
        dummy = ListNode(0)
        node = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
    