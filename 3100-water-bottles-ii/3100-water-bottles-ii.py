class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        bottlesDrunk = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange - 1
            numExchange += 1
            bottlesDrunk += 1
        return bottlesDrunk
        