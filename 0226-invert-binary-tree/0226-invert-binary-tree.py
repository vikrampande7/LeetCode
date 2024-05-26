# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            - Check the edge case of Null
            - Use DFS -> Recursion
            - Swap the Left and Right nodes
            - Use recursion after that
        """
        
        if root is None:
            return None
        
        # Swap nodes    
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursion on childer
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root