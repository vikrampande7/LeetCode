class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(minHeap, (d, i))
        res = []
        for i in range(k):
            d, i = heapq.heappop(minHeap)
            res.append(points[i])
        return res