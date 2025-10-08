class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stonesMap = {}
        j = 0
        for stone in stones:
            stonesMap[stone] = stonesMap.get(stone, 0) + 1
        for jewel in jewels:
            if jewel in stonesMap:
                j += stonesMap[jewel]
        return j
        