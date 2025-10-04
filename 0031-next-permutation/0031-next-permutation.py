class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break

        # if the index is still -1, that means we have to reverse the whole array
        if idx == -1:
            nums.reverse()
            return

        # Find the element just greater than the element at index idx
        for i in range(n-1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        # Once the element is in the original position, reverse the array after that element
        l, r = idx+1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1    