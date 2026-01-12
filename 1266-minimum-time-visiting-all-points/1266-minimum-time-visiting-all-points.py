class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        d = 0
        for i in range(len(points)-1):
            curr_X, curr_Y = points[i]
            next_X, next_Y = points[i+1]
            d += max(abs(curr_X-next_X), abs(curr_Y-next_Y))
        return d
        