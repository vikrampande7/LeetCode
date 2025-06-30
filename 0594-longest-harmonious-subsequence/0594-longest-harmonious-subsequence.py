class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        result = 0

        for num in nums:
            mp[num] += 1

        for num in nums:
            minNum = num
            maxNum = num + 1

            if maxNum in mp:
                result = max(result, mp[minNum] + mp[maxNum])

        return result