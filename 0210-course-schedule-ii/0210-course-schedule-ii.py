class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        for c, p in prerequisites:
            prereq[c].append(p)

        res = []
        visit, cycle = set(), set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True

            cycle.add(node)
            for p in prereq[node]:
                if dfs(p) == False:
                    return False
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res
        