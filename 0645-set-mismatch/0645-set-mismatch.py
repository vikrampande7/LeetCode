class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] > 1:
                res.append(n)
                break
        for i in range(1, len(nums)+1):
            if i not in nums:
                res.append(i)
        return res 
        