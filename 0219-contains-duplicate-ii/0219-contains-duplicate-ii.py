class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        diffMap = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in diffMap and i - diffMap[n] <= k:
                return True
            diffMap[n] = i
        return False