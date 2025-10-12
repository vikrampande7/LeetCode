class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirs:
                    R, C = row + dr, col + dc
                    if (R in range(ROWS) and C in range(COLS) and (R, C) not in visit and grid[R][C] == "1"):
                        visit.add((R, C))
                        q.append((R, C))

        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands