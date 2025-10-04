class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr_string, left_count, right_count):
            if len(curr_string) == 2*n:
                res.append("".join(curr_string))
                return
            if left_count < n:
                curr_string.append("(")
                curr_string.pop()
                backtrack(curr_string, left_count + 1, right_count)
            if left_count > right_count:
                curr_string.append(")")
                backtrack(curr_string, left_count, right_count + 1)
                curr_string.pop()
        backtrack([], 0, 0)
        return res
                
        