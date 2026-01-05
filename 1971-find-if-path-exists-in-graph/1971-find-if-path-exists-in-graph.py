class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        visited = set()
        visited.add(source)
        stack = [source]

        from_to_map = defaultdict(list)
        for f, t in edges:
            from_to_map[f].append(t)
            from_to_map[t].append(f)
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei in from_to_map[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
        return False