class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = Counter(tasks)
        maxHeap = [-freq for freq in counts.values()] 
        heapq.heapify(maxHeap)
        waiting_q = deque()
        time = 0

        while maxHeap or waiting_q:
            time += 1

            if maxHeap:
                f = heapq.heappop(maxHeap) + 1
                if f:
                    waiting_q.append([f, time + n])

            if waiting_q and waiting_q[0][1] == time:
                heapq.heappush(maxHeap, waiting_q.popleft()[0])

        return time