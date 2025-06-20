# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []

        def getVal(node):
            if node is None:
                return None
            lst.append(node.val)
            getVal(node.left)
            getVal(node.right)

        
        getVal(root)
        lst.sort()

        return lst[k-1]
        