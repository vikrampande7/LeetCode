class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)

        for num in nums:
            if num == largest:
                continue
            if num * 2 <= largest:
                continue
            else:
                return -1

        idx = 0
        for i in range(len(nums)):
            if nums[i] == largest:
                idx = i

        return idx