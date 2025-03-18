class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(n^2)

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]:
                continue
        
            l = i + 1
            r = len(nums) - 1

            while l < r:
                ts = v + nums[l] + nums[r]

                if ts > 0:
                    r -= 1
                elif ts < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l-1] and l < r:
                        l += 1
            
        return res
        