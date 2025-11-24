class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            first = -1 * heapq.heappop(heap)
            second = -1 * heapq.heappop(heap)
            if second < first:
                diff = first - second
                heapq.heappush(heap, -diff)
        return -heap[0] if heap else 0