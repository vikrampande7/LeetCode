class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        for i in range(len(points)):
            x, y = points[i]
            dst = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dst, i))
        out = []
        for _ in range(k):
            dst, idx = heapq.heappop(heap)
            out.append(points[idx])
        return out