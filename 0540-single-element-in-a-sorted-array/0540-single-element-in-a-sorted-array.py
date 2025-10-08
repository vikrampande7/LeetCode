class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #### O(n), O(n)
        # hashmap = {}
        # for n in nums:
        #     hashmap[n] = hashmap.get(n, 0) + 1
        # for k, v in hashmap.items():
        #     if v == 1:
        #         return k

        # Binary Search O(logn), O(1)
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if m % 2 == 1:
                m -= 1
            if nums[m] == nums[m+1]:
                l = m + 2
            else:
                r = m
        return nums[l]