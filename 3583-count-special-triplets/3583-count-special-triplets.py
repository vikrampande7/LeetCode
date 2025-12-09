class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # MOD = 10**9 + 7
        # freqBefore, freqAfter = {}, {}
        # for i in range(len(nums)):
        #     targetBefore = nums[i] * 2
        #     countBefore = nums[:i].count(targetBefore)
        #     freqBefore[i] = countBefore

        #     targetAfter = nums[i] * 2
        #     countAfter = nums[i+1:].count(targetAfter)
        #     freqAfter[i] = countAfter
        # triplets = 0
        # for i in range(len(nums)):
        #     triplets = (triplets + (freqBefore[i] * freqAfter[i]) % MOD) % MOD
        # return triplets
        MOD = 10**9 + 7
        num_cnt = {}
        num_partial_cnt = {}

        for v in nums:
            num_cnt[v] = num_cnt.get(v, 0) + 1

        ans = 0
        for v in nums:
            target = v * 2
            l_cnt = num_partial_cnt.get(target, 0)
            num_partial_cnt[v] = num_partial_cnt.get(v, 0) + 1
            r_cnt = num_cnt.get(target, 0) - num_partial_cnt.get(target, 0)
            ans = (ans + l_cnt * r_cnt) % MOD

        return ans