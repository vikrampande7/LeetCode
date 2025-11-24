class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap, out = [], 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush(minHeap, matrix[r][c])        
        for i in range(k):
            out = heapq.heappop(minHeap)
        return out