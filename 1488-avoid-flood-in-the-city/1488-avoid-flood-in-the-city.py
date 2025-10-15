class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [1] * n
        sunnyDays = SortedList()
        fullLakes = {}

        for i, rain in enumerate(rains):
            if rain == 0:
                sunnyDays.add(i)
                continue
            else:
                ans[i] = -1
                if rain in fullLakes:
                    lastRainDay = fullLakes[rain]
                    idx = sunnyDays.bisect_right(lastRainDay) # Find rightmost index 
                    if idx == len(sunnyDays):
                        return []
                
                    dryDay = sunnyDays[idx]
                    ans[dryDay] = rain
                    sunnyDays.remove(dryDay)

            fullLakes[rain] = i
        
        return ans