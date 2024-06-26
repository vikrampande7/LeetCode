# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            - Check if root is greater than or less than left and right children
            - Set up the boundaries - Negative and Positive for comparison
            - Borrow the boundaries from parents for comparison when root is child
            - Recursion on left and right
        """
        
        def isValid(root, left, right):
            
            if not root:
                return True
            
            if not (root.val < right and root.val > left):
                return False
            
            return (isValid(root.left, left, root.val) and isValid(root.right, root.val, right))
        
        return isValid(root, float("-inf"), float("inf"))
            
            