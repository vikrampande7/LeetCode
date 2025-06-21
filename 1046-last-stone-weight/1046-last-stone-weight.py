class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for s in stones:
            heapq.heappush(maxHeap, -s)

        while len(maxHeap) > 1:    
            f = heapq.heappop(maxHeap)
            s = heapq.heappop(maxHeap)
            if f < s:
                diff = f - s
                heapq.heappush(maxHeap, diff)

        return -maxHeap[0] if maxHeap else 0
        