class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        lastEle = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], lastEle = lastEle, max(lastEle, arr[i])
        return arr
        