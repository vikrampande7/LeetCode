class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # -4 -1 -1 0 1 2

        # -4 + -1 + 2 = -4 - 1 + 2 = -3 < 0, increasee left pointer, but same as -1 so increase again
        # -4 + 0 + 2 = -2 < 0 increase 
        # -4 + 1 + 2 = -1 < 0 NO PAIR

        # -1 + -1 + 2 = -1 - 1 + 2 = 0 == 0 Found a pair

        # -1 + 0 + 2 = 1 > 0, reduce right pointer
        # -1 + 0 + 1 = 0 == found pair

        nums.sort()
        out = []

        for fixed in range(len(nums) - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue 
            l = fixed + 1
            r = len(nums) - 1
            while l < r:
                triplet_sum = nums[fixed] + nums[l] + nums[r]
                if triplet_sum > 0:
                    r -= 1
                elif triplet_sum < 0:
                    l += 1
                else:
                    out.append([nums[fixed], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1          
        return out