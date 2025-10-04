class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = {}
        ans = []
        
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1
        
        for n, f in countMap.items():
            if f > len(nums) / 3:
                ans.append(n)
        
        return ans