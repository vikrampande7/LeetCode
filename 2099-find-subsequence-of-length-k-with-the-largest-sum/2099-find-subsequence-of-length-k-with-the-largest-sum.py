class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

        res = []
        for i in range(k):
            _, idx = heapq.heappop(heap)
            res.append(idx)

        res.sort()

        return [nums[i] for i in res]

        