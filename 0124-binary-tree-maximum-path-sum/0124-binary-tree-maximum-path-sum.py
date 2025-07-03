# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            left_val = dfs(node.left)
            right_val = dfs(node.right)
            left_val = max(left_val, 0)
            right_val = max(right_val, 0)

            res[0] = max(res[0], node.val + left_val + right_val)
            return node.val + max(left_val, right_val)

        dfs(root)
        return res[0]