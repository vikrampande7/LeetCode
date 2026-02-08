class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = {i: 0 for i in range(1, n+1)} # How many courses have 0 prereq, only can take those courses
        
        for prer, nextc in relations:
            graph[prer].append(nextc)
            in_degree[nextc] += 1
        
        taken = set()
        minSem = 0
        q = deque()
        
        q = deque([course for course in in_degree if in_degree[course] == 0])

        while q:
            minSem += 1
            for i in range(len(q)):
                course = q.popleft()
                taken.add(course)
                for nei in graph[course]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0: # Cycle
                        q.append(nei)
                
        return minSem if len(taken) == n else -1