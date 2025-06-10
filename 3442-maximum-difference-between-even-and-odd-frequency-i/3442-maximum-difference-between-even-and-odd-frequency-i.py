class Solution:
    def maxDifference(self, s: str) -> int:
        countMap = {}
        for c in s:
            countMap[c] = countMap.get(c, 0) + 1

        evenMin, oddMax = float('inf'), 0
        for k, v in countMap.items():
            if v % 2 == 0:
                evenMin = min(evenMin, v)
            if v % 2 != 0:
                oddMax = max(oddMax, v)
            
        return oddMax-evenMin 
        