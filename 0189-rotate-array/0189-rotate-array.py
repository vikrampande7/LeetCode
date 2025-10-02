class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            last = nums[-1]
            for i in range(len(nums)):
                nums[i], last = last, nums[i]
        
        