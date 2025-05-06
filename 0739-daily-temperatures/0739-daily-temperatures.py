class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ## Recursion
        # ans = []

        # def recursion(l, r):
        #     if r == len(temperatures):
        #         ans.append(0)
        #         return
            
        #     if temperatures[l] < temperatures[r]:
        #         ans.append(r - l)
        #     else:
        #         recursion(l, r+1)

        # for i in range(len(temperatures)):
        #     recursion(i, i+1)

        # return ans

        n = len(temperatures)
        stack = []
        ans = [0]*n
        
        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
        
            if not stack:
                ans[i] = 0 
            else:
                ans[i] = stack[-1] - i
            stack.append(i)
        
        return ans

            