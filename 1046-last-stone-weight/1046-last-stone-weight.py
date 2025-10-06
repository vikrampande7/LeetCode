class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        print(maxHeap)
        while len(maxHeap) > 1:
            first = -1 * heapq.heappop(maxHeap)
            secon = -1 * heapq.heappop(maxHeap)
            if secon < first:
                diff = first - secon
                heapq.heappush(maxHeap, -diff)
        return -maxHeap[0] if maxHeap else 0
        