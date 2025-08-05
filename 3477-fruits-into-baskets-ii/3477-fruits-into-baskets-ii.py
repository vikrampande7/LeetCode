class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for f in range(len(fruits)):
            for b in range(len(baskets)):
                if fruits[f] <= baskets[b]:
                    baskets.remove(baskets[b])
                    break
        return len(baskets)
        