class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(r, c):
            q = deque([(r, c)])
            visit.add((r, c))
            while q:
                r, c = q.popleft()
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for R, C in dirs:
                    if (r+R in range(ROWS)) and (c+C in range(COLS)) and ((r+R, c+C) not in visit) and (grid[r+R][c+C] == "1"):
                        q.append((r+R, c+C))
                        visit.add((r+R, c+C))
        if not grid:
            return 0
        islands = 0 
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands