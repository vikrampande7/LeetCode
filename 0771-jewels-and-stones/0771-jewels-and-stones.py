class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_map = {}
        res = 0
        for c in stones:
            stones_map[c] = stones_map.get(c, 0) + 1
        for c in jewels:
            if c in stones_map:
                res += stones_map[c]
        return res