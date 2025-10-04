class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            m = (low + high) // 2    
            hrs_spent = 0  
            for p in piles:
                hrs_spent += math.ceil(p / m)
            
            if hrs_spent <= h:
                high = m
            else:
                low = m + 1
        print(9//2)
        return high