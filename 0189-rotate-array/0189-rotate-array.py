class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### Brute Force - O(nk), O(1)
        # k = k % len(nums)
        # for _ in range(k):
        #     last = nums[-1]
        #     for i in range(len(nums)):
        #         nums[i], last = last, nums[i]      

        ### With Extra Space O(n), O(n)
        # n = len(nums)
        # a = [0] * n
        # for i in range(n):
        #     a[(i+k) % n] = nums[i]
        # nums[:] = a

        ### With Reverse O(1) SC and O(n) TC
        def helper(nums, s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s, e = s + 1, e - 1

        n = len(nums)
        k = k % n

        helper(nums, 0, n-1)
        helper(nums, 0, k-1)
        helper(nums, k, n-1)