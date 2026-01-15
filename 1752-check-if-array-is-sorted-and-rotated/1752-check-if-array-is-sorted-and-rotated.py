class Solution:
    def check(self, nums: List[int]) -> bool:
        def isSorted(arr, n):
            for i in range(1, n):
                if arr[i] < arr[i - 1]:  
                    return False
            return True
        n = len(nums)
        for i in range(n):
            x %= i
            b = nums[x:] + nums[:x]
            if isSorted(b, n):
                return True
        return False
        