# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # 定义一个辅助函数，携带上界和下界
        def validate(node, low=float('-inf'), high=float('inf')):
            # 空节点也是合法的 BST
            if not node:
                return True
            
            # 核心判断：如果当前节点的值超出了允许的范围，直接 False
            if node.val <= low or node.val >= high:
                return False
            
            # 递归验证左右子树，注意更新边界：
            # 往左走，当前节点的值变成最大上限 (high)
            # 往右走，当前节点的值变成最小下限 (low)
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        return validate(root)