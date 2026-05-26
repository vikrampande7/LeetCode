class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        connections = {
            1: [(0,-1),(0,1)],
            2: [(-1,0),(1,0)],
            3: [(0,-1),(1,0)],
            4: [(0,1),(1,0)],
            5: [(0,-1),(-1,0)],
            6: [(0,1),(-1,0)]
        }

        visited = set()
        visited.add((0, 0))
        queue = deque([(0, 0)])

        while queue:
            r, c = queue.popleft()

            if r == ROWS - 1 and c == COLS - 1:
                return True

            for dr, dc in connections[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    for ndr, ndc in connections[grid[nr][nc]]:
                        if ndr + nr == r and ndc + nc == c:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
        return False