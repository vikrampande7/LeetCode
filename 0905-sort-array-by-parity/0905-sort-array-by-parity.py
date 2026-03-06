class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        out = []
        for n in nums:
            if n % 2 == 0:
                out.append(n)
        for n in nums:
            if n % 2 != 0:
                out.append(n)
        return out