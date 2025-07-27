class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        l =0 
        count = 0
        n = len(nums)

        for i in range(1, n-1):
            if nums[i] != nums[i+1]:
                if (nums[l] < nums[i] and nums[i+1] < nums[i]) or (nums[l] > nums[i] and nums[i+1] > nums[i]):
                    count += 1
                l = i
        
        return count


        