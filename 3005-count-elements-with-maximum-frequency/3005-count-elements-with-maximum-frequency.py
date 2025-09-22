class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        sorted_items = sorted(freqMap.items(), key=lambda item: item[1], reverse=True)
        sortedFreqMap = dict(sorted_items)
        maxFreq = next(iter(sortedFreqMap.values()))
        res = 0
        for k, v in sortedFreqMap.items():
            if v == maxFreq:
                res += v
        return res