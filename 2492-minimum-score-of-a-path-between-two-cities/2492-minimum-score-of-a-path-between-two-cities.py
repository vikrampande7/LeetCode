class Solution(object):
    def bfs(self, n, adj):
        visit = [False] * (n + 1)
        q = deque()
        answer = float('inf')

        q.append(1)
        visit[1] = True

        while q:
            node = q.popleft()

            for neighbor, weight in adj[node]:
                answer = min(answer, weight)
                if not visit[neighbor]:
                    visit[neighbor] = True
                    q.append(neighbor)
                    
        return answer

    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
            
        return self.bfs(n, adj)
        