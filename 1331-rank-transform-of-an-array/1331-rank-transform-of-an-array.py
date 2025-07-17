class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        cp = sorted(set(arr))
        rankMap = {}

        for i in range(len(cp)):
            if cp[i] not in rankMap:
                rankMap[cp[i]] = i+1

        out = [rankMap.get(num) for num in arr]

        return out