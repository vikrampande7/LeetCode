# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return '#'
            left_s = dfs(node.left)
            right_s = dfs(node.right)

            signature = f"{node.val},{left_s},{right_s}"

            count[signature] += 1

            if count[signature] == 2:
                res.append(node)

            return signature

        dfs(root)
        return res