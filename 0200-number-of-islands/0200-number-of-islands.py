"""
    DFS and mark when visited
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        VISITED = set()
        islandCount = 0
        
        def dfs(r, c):
            if (r < 0 
            or c < 0
            or r == ROWS
            or c == COLS
            or (r,c) in VISITED 
            or grid[r][c] == "0"):
                return
            
            VISITED.add((r, c))
            DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in DIRS:
                dfs(r+dr, c+dc)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in VISITED:
                    islandCount += 1
                    dfs(r, c)
                    
        return islandCount
                
        
                    
        