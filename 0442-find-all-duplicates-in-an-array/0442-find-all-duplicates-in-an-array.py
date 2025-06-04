class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        countMap = {}
        for i in nums:
            countMap[i] = countMap.get(i, 0) + 1

        arr = []
        for i in countMap:
            if countMap[i] == 2:
                arr.append(i)
        
        return arr