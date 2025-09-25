class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minSumPath = []
        for t in triangle:
            minSumPath.append(min(t))
        return sum(minSumPath)
        