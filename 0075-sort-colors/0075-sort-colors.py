class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, c = 0, 0
        r = len(nums) - 1

        while c <= r:
            if nums[c] == 0:
                nums[l], nums[c] = nums[c], nums[l]
                c += 1
                l += 1
            elif nums[c] == 2:
                nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            else:
                c += 1


        