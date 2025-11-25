class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # for i in range(len(heights)-1):
        #     if heights[i+1] > heights[i]:
        #         if bricks >= heights[i+1] - heights[i] and bricks > 0:
        #             bricks -= (heights[i+1] - heights[i])
        #         elif ladders > 0:
        #             ladders -= 1
        #         else:
        #             return i
        # return i+1

        # MinHeap Approach
        minHeap = []
        for i in range(len(heights) - 1):
            climb = heights[i+1] - heights[i]
            if climb > 0:
                heapq.heappush(minHeap, climb)
            if len(minHeap) > ladders:
                bricks -= heapq.heappop(minHeap)
            if bricks < 0:
                return i
        return len(heights) - 1