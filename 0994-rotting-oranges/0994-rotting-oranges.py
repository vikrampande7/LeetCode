class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        Q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    Q.append((r, c))

        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while Q and fresh > 0:
            for o in range(len(Q)):
                r,c = Q.popleft()

                for dr, dc in DIR:
                    row = r + dr
                    col = c + dc

                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        grid[row][col] = 2
                        Q.append((row, col))
                        fresh -= 1

            time += 1

        return -1 if fresh > 0 else time