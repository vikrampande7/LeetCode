class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        atl, pac = set(), set()
        out = []

        def dfs(r, c, visit, ph):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < ph or (r, c) in visit):
                return

            visit.add((r, c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # First row, all columns
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # Last row, all columns

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # First col, all rows
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # Last col, all rows

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atl and (r, c) in pac:
                    out.append([r, c])

        return out