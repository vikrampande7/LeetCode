class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        distinct = set()

        for num in nums:
            if num < k:
                return -1
            elif num > k:
                distinct.add(num)

        return len(distinct)
            
        