class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        for v in hm.values():
            if v >= 2:
                return True
        return False
        