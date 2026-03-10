class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1
        res = []
        for num in range(1, len(nums) + 1):
            if num not in hashMap:
                res.append(num)
        return res