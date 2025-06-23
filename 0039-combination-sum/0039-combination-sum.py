class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recursion(i, tmp, targetSum):
            if targetSum == target:
                res.append(tmp[:])
                return
            if i >= len(candidates) or targetSum > target:
                return

            tmp.append(candidates[i])
            recursion(i, tmp, targetSum+candidates[i]) # Include current index
            tmp.pop()
            recursion(i+1, tmp, targetSum) # Do not include current index

        recursion(i=0, tmp=[], targetSum=0)

        return res