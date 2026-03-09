class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        if len(arr) < 3:
            return max(arr)
        arr.sort(reverse=True)
        return arr[2]