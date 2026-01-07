# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []
        def tree_sum(subroot):
            if subroot is None:
                return 0
            left_sum = tree_sum(subroot.left)
            right_sum = tree_sum(subroot.right)
            total = subroot.val + left_sum + right_sum
            all_sums.append(total)
            return total
        total = tree_sum(root)
        ans = 0
        for s in all_sums:
            ans = max(ans, s * (total-s))
        return ans  % (10 ** 9 + 7)