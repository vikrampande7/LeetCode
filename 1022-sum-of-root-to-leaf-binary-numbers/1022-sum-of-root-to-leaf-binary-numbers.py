# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        allPaths = []
        def dfs_helper(node, currentPath):
            if not node:
                return
            currentPath.append(str(node.val))
            if not node.left and not node.right:
                allPaths.append("".join(currentPath))
            else:
                dfs_helper(node.left, currentPath)
                dfs_helper(node.right, currentPath)
            currentPath.pop()
        dfs_helper(root, [])
        out = 0
        for p in allPaths:
            out += int(p, 2)
        return out
        