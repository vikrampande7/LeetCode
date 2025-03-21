class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # Assume left and right have no plants, then check if prev, current and next are 0 i.e. no plant, if not, plant the flowers
        # decrease n

        fb = [0] + flowerbed + [0]

        for i in range(1, len(fb)-1):
            if fb[i-1] == 0 and fb[i] == 0 and fb[i+1] == 0:
                fb[i] = 1
                n -= 1

        return n <= 0
        