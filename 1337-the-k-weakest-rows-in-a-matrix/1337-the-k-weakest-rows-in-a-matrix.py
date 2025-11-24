class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for r in range(len(mat)):
            soldiers = 0
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    soldiers += 1
            heapq.heappush(heap, (soldiers, r))
        res = []
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            res.append(idx)
        return res
        