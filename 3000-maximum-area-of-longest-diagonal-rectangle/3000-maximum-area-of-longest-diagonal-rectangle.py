class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        heap = []
        for l, w in dimensions:
            diag_sq = (l*l) + (w*w)
            diag = math.sqrt(diag_sq)
            area = l * w
            heapq.heappush(heap, (-diag, -area))
        d, a = heapq.heappop(heap)
        return -a