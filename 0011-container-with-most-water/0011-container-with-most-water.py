class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Bruteforce Solution: Using two loops but time complexity is o(n**2)
        area = 0 
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                a = min(height[i],height[j]) * (i-j) # breadth * minimum(length)
                area = max(a, area)
        return area
        
        But to do this in o(n)
        - We just check the broader breadth
        - For that if left pointer is less than right pointer we shift out left pointer to right 
        - and vice versa
        - so that we would maximize the area
        '''
        area = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            a = min(height[l],height[r]) * (r-l) # breadth * minimum(length)
            area = max(a, area)
            
            if height[l] < height[r]:
                l += 1
            elif height[l] < height[r]:
                r -= 1
            else:
                r -= 1
                
        return area
        