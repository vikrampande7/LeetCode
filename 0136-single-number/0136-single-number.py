class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = {}
        for num in nums:
            hashSet[num] = hashSet.get(num, 0) + 1
        
        for k, v in hashSet.items():
            if v == 1:
                return k
        