class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        fresh = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    R, C = row+dr, col+dc        
                    if R in range(ROWS) amd C in range(COLS) and grid[R][C] == 1:
                        grid[R][C] = 2
                        fresh -= 1
            time += 1 
    
        return -1 if fresh > 0 else time