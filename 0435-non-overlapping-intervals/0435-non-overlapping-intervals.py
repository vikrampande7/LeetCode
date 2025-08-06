class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt = 0
        prevEnd = intervals[0][1]
        for s, e in intervals[1:]:
            if s >= prevEnd:
                prevEnd = e
            else:
                cnt += 1
                prevEnd = min(e, prevEnd)
        return cnt