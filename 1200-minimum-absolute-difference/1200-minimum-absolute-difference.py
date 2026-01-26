class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        minDiff = float('inf')
        for i in range(len(arr) - 1):
            minDiff = min(minDiff, arr[i + 1] - arr[i])
        for a in range(len(arr)-1):
            if abs(arr[a+1]-arr[a]) == minDiff:
                    ans.append([arr[a], arr[a+1]])
        return ans