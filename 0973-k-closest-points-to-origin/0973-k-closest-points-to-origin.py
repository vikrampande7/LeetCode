class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x, y):
            x_ = abs(x-0)
            y_ = abs(y-0)
            d = math.sqrt((x_**2)+(y_**2))
            return d

        heap = []
        for point in points:
            d = getDistance(point[0], point[1])
            heapq.heappush(heap, (d, point))
        
        result = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            result.append(point)
        
        return result
        