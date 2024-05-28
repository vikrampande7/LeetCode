# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
            - If both trees are empty, they are same
            - If one of the tree is null, they are not same
            - If nodes containing values are not same, return False
            - Recursion on Left and Right node:
        """
        
        if not p and not q:
            return True
        
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        
        