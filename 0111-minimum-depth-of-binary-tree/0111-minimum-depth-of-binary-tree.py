# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        minLen = float("inf")
        level = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                if not node.left and not node.right:
                    return level
                q.append(node.left)
                q.append(node.right)
            level += 1
        return level