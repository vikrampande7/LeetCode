class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix)m len(matrix[0])
        cache = {}
        
        def dfs(r, c, prev):
            if (r<0 or r==ROWS or c<0 or c==COLS or matrix[r][c] <= prev):
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            lp = 0
            lp = max(lp ,1 + dfs(r+1, c, matrix[r][c]))
            lp = max(lp ,1 + dfs(r-1, c, matrix[r][c]))
            lp = max(lp ,1 + dfs(r, c+1, matrix[r][c]))
            lp = max(lp ,1 + dfs(r, c-1, matrix[r][c]))
            cache[(r, c)] = lp
            return lp
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(cache.values())