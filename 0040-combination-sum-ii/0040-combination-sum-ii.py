class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def recursion(i, tmp, targetSum):
            if targetSum == target:
                res.append(tmp[:])
                return
            if i >= len(candidates) or targetSum > target:
                return

            tmp.append(candidates[i])
            recursion(i+1, tmp, targetSum+candidates[i])
            tmp.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]: # If element is equal, go forward by 1
                i += 1
            recursion(i+1, tmp, targetSum)

        recursion(i=0, tmp=[], targetSum=0)

        return res