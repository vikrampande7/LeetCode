class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        

    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = nums
        

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums.sort()
    #     return self.nums[len(self.nums) - self.k]
        
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)