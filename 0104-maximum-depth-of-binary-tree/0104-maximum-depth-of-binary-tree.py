# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        - DFS Recursive
            - Check edge of when tree is null
            - Otherwise if 1 root, sum is one
            - Check for the children (left and right), add maximum length of connecting nodes
        - DFS Iterative
        - BFS Iterative
        """
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))