class Solution:
    def canMakeB(self, bloomDay: List[int], mid: int, k: int) -> int:
        bqCount, consecutiveCount = 0, 0
        
        for i in range(len(bloomDay)):
            if bloomDay[i] <= mid:
                consecutiveCount += 1
            else:
                consecutiveCount = 0
                
            if consecutiveCount == k:
                bqCount += 1
                consecutiveCount = 0
                
        return bqCount
    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        start_day = 0
        end_day = max(bloomDay)
        minDays = -1
        
        while start_day <= end_day:
            mid = start_day + (end_day - start_day) // 2
            
            if self.canMakeB(bloomDay, mid, k) >= m:
                minDays = mid
                end_day = mid - 1
            else:
                start_day = mid + 1
                
        return minDays