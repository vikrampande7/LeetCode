# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return []
        res = None
        def recursion(node):
            nonlocal res
            if node.val == val:
                res = node
                return
            if node.left:
                recursion(node.left)
            if node.right:
                recursion(node.right)
            return []
        recursion(root)
        return res
        
        
        