class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def validCell(grid, i, j):
            n = len(grid)
            return 0 <= i < n and 0 <= j < n

        def validSafeness(grid, min_safeness):
            n = len(grid)
            if grid[0][0] < min_safeness or grid[n-1][n-1] < min_safeness:
                return False
            travQ = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            while travQ:
                curr = travQ.popleft()
                if curr[0] == n-1 and curr[1] == n-1:
                    return True
                for d in dirs:
                    di, dj = curr[0] + d[0], curr[1] + d[1]
                    if validCell(grid, di, dj) and not visited[di][dj] and grid[di][dj] >= min_safeness:
                        visited[di][dj] = True
                        travQ.append((di, dj))
            return False


        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        while q:
            s = len(q)
            while s > 0:
                curr_i, curr_j = q.popleft()
                for d_i, d_j in dirs:
                    nei_i, nei_j = curr_i + d_i, curr_j + d_j
                    val = grid[curr_i][curr_j]
                    if validCell(grid, nei_i, nei_j) and grid[nei_i][nei_j] == -1:
                        grid[nei_i][nei_j] = val + 1
                        q.append((nei_i, nei_j))
                s -= 1

        l, r, res = 0, 0, -1
        for i in range(n):
            for j in range(n):
                r = max(r, grid[i][j])
        while l <= r:
            mid = l + (r - l) // 2
            if validSafeness(grid, mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res