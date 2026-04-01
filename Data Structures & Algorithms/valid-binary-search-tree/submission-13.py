# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack =[]
        curr = root
        prev = -1001
        
        # 当栈不为空，或者当前节点不为空时，继续遍历
        while stack or curr:
            # 1. 一路向左钻到底，把左侧节点全部压入栈
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. 弹出栈顶节点（这是目前能访问到的最小的节点）
            curr = stack.pop()
            if curr.val <= prev:
                return False
            prev = curr.val
            
            # 3. 转向右子树
            curr = curr.right
            
        return True