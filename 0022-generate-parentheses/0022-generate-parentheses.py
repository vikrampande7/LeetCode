class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(openCnt, closedCnt):
            if openCnt == closedCnt == n:
                res.append("".join(stack))
                return
            
            if openCnt < n:
                stack.append("(")
                backtrack(openCnt+1, closedCnt)
                stack.pop()
                
            if closedCnt < openCnt:
                stack.append(")")
                backtrack(openCnt, closedCnt+1)
                stack.pop()
                
        backtrack(0, 0)
        return res
        