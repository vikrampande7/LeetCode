class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = []
        for s in spells:
            l = 0
            r = n
            while l < r:
                m = (l + r) // 2
                if potions[m] * s < success:
                    l = m + 1
                else:
                    r = m
            res.append(n - l)
        return res