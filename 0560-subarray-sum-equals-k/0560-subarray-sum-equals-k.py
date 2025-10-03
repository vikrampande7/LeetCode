class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        prefixSumMap = {0:1}
        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSumMap[diff] if prefixSumMap[diff] else 0
            prefixSumMap[currSum] = prefixSumMap.get(currSum, 0) + 1
        return res