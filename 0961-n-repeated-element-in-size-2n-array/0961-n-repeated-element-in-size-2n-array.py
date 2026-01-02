class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        elements = {}
        for n in nums:
            elements[n] = elements.get(n, 0) + 1
        for k, v in elements.items():
            if v > 1:
                return k
        