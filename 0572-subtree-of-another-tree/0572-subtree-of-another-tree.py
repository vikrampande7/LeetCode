# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
            - If root and subroot are empty, return False
            - Recursion -> Input left and right nodes of Tree
            - If root.val and subroot.val are not equal return False
            - If root.left and subroot.left are not equal return False
        """
        if not subRoot:
            return True
        
        if not root:
            return False
     
        if self.checkSameTree(root, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        
    
    def checkSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        
        
        if t1 and t2 and t1.val == t2.val:
            if self.checkSameTree(t1.left, t2.left) and self.checkSameTree(t1.right, t2.right):
                return True
        

        return False
        