# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        level_sum = {}
        q = deque([root])
        curr_level = 1
        while q:
            curr_sum = 0
            for i in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_sum = max(max_sum, curr_sum) 
            level_sum[curr_level] = curr_sum
            curr_level += 1
        for k, v in level_sum.items():
            if v == max_sum:
                return k