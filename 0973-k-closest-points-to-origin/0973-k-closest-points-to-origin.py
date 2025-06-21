class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashMap = {}
        minHeap = []
        out = []

        def getDistance(x, y):
            x_ = abs(x-0)
            y_ = abs(y-0)
            d = math.sqrt((x_**2)+(y_**2))
            return d

        for p in points:
            d = getDistance(p[0],p[1])
            hashMap[d] = p
            minHeap.append(d)
            
        minHeap.sort()

        for d in minHeap:
            out.append(hashMap[d])

        return out[:k]
        