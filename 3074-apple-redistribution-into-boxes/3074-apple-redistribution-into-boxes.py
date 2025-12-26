class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApples = sum(apple)
        count, apples = 0, 0
        heap = []
        for cap in capacity:
            heapq.heappush(heap, -cap)
        while True:
            if apples >= totalApples:
                return count
            topCap = -1 * heapq.heappop(heap)
            apples += topCap
            count += 1
        return count