class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        n = 0
        for s in range(len(heights)):
            if heights[s] != expected[s]:
                n += 1
        return n