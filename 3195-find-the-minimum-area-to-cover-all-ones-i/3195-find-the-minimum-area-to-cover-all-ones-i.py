class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        maxRow = 0 
        maxCol = 0
        minRow = float('inf')
        minCol = float('inf')
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    minCol = min(minCol, c)
                    minRow = min(minRow, r)
                    maxCol = max(maxCol, c)
                    maxRow = max(maxRow, r)
        h = maxRow - minRow + 1
        w = maxCol - minCol + 1

        return h * w 