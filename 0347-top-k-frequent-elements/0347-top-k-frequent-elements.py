class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        heap, out = [], []
        for k, v in hashmap.items():
            heapq.heappush(heap, (-v, k))
        for i in range(k-1):
            freq, val = heapq.heappop(heap)
            out.append(val)
        return out