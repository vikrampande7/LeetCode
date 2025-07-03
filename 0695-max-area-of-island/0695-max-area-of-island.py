class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if (r == ROWS or c == COLS or r < 0 or c < 0 or (r, c) in VISITED or grid[r][c] == 0):
                return 0

            VISITED.add((r, c))

            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1) )

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        VISITED = set()
        
        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
                    
        return maxArea
        