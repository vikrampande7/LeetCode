class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        for k, v in hashmap.items():
            if v == 1:
                return k