class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)

        n = len(nums)
        count = 0
        currSum = 0
        mp[currSum] = 1

        for i in range(n):
            currSum += (nums[i] % 2)  # if odd - 1, even - 0

            if (currSum - k) in mp:
                count += mp[currSum - k]

            mp[currSum] += 1

        return count
        