class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        minHeap = []
        ans = []
        for num in arr:
            b = str(bin(num))
            ones = b.count("1")
            heapq.heappush(minHeap, (ones, num))
        for i in range(len(minHeap)):
            ones, num = heapq.heappop(minHeap)
            ans.append(num)
        return ans