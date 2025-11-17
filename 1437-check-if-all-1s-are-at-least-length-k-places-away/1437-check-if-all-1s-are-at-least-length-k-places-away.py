class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(i)
        for i in range(len(ones) - 1):
            if (ones[i+1] - ones[i]) <= k:
                return False
        return True