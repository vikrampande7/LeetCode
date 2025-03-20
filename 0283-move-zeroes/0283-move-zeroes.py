class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            # Iterate in reverse order for 1 step
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

        