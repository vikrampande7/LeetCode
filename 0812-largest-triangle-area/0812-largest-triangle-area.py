class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        largestArea = 0
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    
                    area = 0.5 * abs(
                        x1 * (y2-y3) + x2 * (y1-y3) + x3 * (y1-y2)
                    )

                    largestArea = max(area, largestArea)
        return largestArea
        