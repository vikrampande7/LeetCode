# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        out = []

        def level_order(node, level):
            if not node:
                return []
            
            if level >= len(out):
                out.append([])

            out[level].append(node.val)
            level_order(node.left, level+1)
            level_order(node.right, level+1)

        level_order(root, 0)

        return out
        