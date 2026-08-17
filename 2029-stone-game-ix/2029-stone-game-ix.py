class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        a = b = c = 0
        for stone in stones:
            if stone % 3 == 0:
                a += 1
            elif stone % 3 == 1:
                b += 1
            else:
                c += 1
        if a % 2 == 0:
            return b >= 1 and c >= 1
        return b - c > 2 or c - b > 2