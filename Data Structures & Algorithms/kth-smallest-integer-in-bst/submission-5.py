class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack =[]
        curr = root
        
        # 当栈不为空，或者当前节点不为空时，继续遍历
        while stack or curr:
            # 1. 一路向左钻到底，把左侧节点全部压入栈
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 弹出栈顶节点（这是目前能访问到的最小的节点）
            curr = stack.pop()
            
            # 3. 计数器减 1，如果减到 0，说明找到了第 k 小的元素！
            k -= 1
            if k == 0:
                return curr.val
            
            # 4. 转向右子树
            curr = curr.right
            
        return -1