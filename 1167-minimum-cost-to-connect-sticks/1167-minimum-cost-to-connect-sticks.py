class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        minHeap, costs = [], []
        for stick in sticks:
            heapq.heappush(minHeap, stick)
        while len(minHeap) > 1:
            first = heapq.heappop(minHeap)
            second = heapq.heappop(minHeap)
            cost = first + second
            costs.append(cost)
            heapq.heappush(minHeap, cost)
        return sum(costs)