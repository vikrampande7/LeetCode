class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = {0:0, 1:0, 2:0}
        for n in nums:
            hashMap[n] += 1
            
        idx = 0
        for c in range(3):
            while hashMap[c] > 0:
                nums[idx] = c
                idx += 1
                hashMap[c] -= 1