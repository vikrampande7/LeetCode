# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            - LCA is where the split occurs
            - Check the root node and go right or left then return the root
        """
        
        r = root
        
        while r:
            if p.val > r.val and q.val > r.val:
                r = r.right
            elif p.val < r.val and q.val < r.val:
                r = r.left
            else:
                return r
        