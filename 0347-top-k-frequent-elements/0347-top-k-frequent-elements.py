class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = {}

        for n in nums:
            freqCount[n] = freqCount.get(n, 0) + 1

        sorted_items = sorted(freqCount.items(), key=lambda x: x[1], reverse=True)

        return [num for num, freq in sorted_items[:k]]