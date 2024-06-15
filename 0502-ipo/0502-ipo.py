class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        vec = [(capital[i], profits[i]) for i in range(n)]
        
        
        vec.sort()
        i = 0
        max_heap = []
        
        while k>0:
            while i < n and vec[i][0] <= w:
                heappush(max_heap, -vec[i][1])
                i+= 1
                
            if not max_heap:
                break
                
            
            w+= -heappop(max_heap)
            k -= 1
            
            
        return w