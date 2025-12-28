class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negatives = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] < 0:
                    negatives += 1
        return negatives
        