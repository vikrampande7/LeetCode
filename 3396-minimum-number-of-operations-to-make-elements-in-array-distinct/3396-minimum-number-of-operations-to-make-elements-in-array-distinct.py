class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def verify_distinct(i):
            distinct_elements = set()
            for num in nums[i:]:
                if num in distinct_elements:
                    return False
                distinct_elements.add(num)
            return True
        
        count = 0
        for i in range(0, len(nums), 3):
            if verify_distinct(i):
                return count
            count += 1
        
        return count
        