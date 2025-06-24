class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        nums.sort()  # Sort to group duplicates together
        
        def recursion(nums, i, tmp):
            if i >= len(nums):
                res.append(tmp[:])
                return 
            
            # Include current element
            tmp.append(nums[i])
            recursion(nums, i + 1, tmp)
            tmp.pop()
            
            # Skip all duplicates when not including current element
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # Exclude current element (and all its duplicates)
            recursion(nums, i + 1, tmp)
        
        recursion(nums, 0, tmp)
        return res
        
        