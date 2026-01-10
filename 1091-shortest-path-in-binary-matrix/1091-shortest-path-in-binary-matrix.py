class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        r_max = c_max = len(grid) - 1
        dirs = directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        if grid[0][0] != 0 or grid[r_max][c_max] != 0:
            return -1
        
        def get_neighbors(r, c):
            for row, col in dirs:
                r_new = r + row
                c_new = c + col
                if (r_new < 0 
                    or r_new > r_max
                    or c_new < 0 
                    or c_new > c_max):
                    continue
                if grid[r_new][c_new] != 0:
                    continue
                yield (r_new, c_new)

        q = deque([(0, 0, 1)])
        visited = {(0, 0)}
        while q:
            r, c, d = q.popleft()
            if (r, c) == (r_max, c_max):
                return d
            for r_nei, c_nei in get_neighbors(r, c):
                if (r_nei, c_nei) in visited:
                    continue
                visited.add((r_nei, c_nei))
                q.append((r_nei, c_nei, d + 1))
        return -1    