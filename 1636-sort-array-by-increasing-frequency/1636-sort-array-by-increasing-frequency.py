class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        nums = sorted(nums.items(), key=lambda x: (x[1], -x[0]))
        return [num for num, freq in nums for _ in range(freq)]