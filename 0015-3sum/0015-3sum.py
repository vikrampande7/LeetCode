class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            If we use bruteforce with three loops, we would encounter problem with duplicates and time complexity would be -> O(n**3)
            Solution:
                - Sort the given array so as to avoid duplicates, if neighbor duplicate is found, skip that.
                - Get the first element and then solve the problem with TwoSum approach
                - Set up the pointers
                - Set up the conditions for sum <> 0 and update pointers accordingly
                - Look for the edgecases
                - Time Complexity -> o(n**2)
        """
        
        out = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
                
            l, r = i+1, len(nums)-1
            while l<r:
                tS = a + nums[l] + nums[r]
                if tS > 0:
                    r -= 1
                elif tS < 0:
                    l += 1
                else:
                    out.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                        
        return out