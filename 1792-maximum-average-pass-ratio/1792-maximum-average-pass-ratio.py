class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Similar to leetcode 1029
        def maxGain(h, idx):
            currAvg = classes[idx][0] / classes[idx][1]
            newAvg = (classes[idx][0] + 1) / (classes[idx][1] + 1)
            gain = newAvg - currAvg
            heapq.heappush(h, (-gain, idx))
        
        heap = []
        n = len(classes)

        # Append initial states
        for i in range(n):
            maxGain(heap, i)

        while extraStudents > 0:
            _, idx = heapq.heappop(heap)
            # Add one extra student
            classes[idx][0] += 1
            classes[idx][1] += 1
            maxGain(heap, idx)
            extraStudents -= 1

        mapr = 0
        for p, t in classes:
            mapr += (p / t)
        
        return mapr / n