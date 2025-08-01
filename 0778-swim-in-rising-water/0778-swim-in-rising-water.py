class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()

        visit.add((0, 0))

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr == N or nc == N or (nr, nc) in visit):
                    continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, [max(time, grid[nr][nc]), nr, nc])
        