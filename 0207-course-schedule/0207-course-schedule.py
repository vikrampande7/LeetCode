class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        preMap = {c:[] for c in range(numCourses)}
        for c, p in prerequisite:
            preMap[c].append(p)
        def dfs(c):
            if c in visit:
                return False
            if preMap[c] == []:
                return True
            visit.add(c)
            for p in preMap[c]:
                if not dfs(p):
                    return False
            visit.remove(p)
            preMap[c] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True