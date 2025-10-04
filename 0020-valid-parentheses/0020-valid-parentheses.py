class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack:
                    top = stack[-1]
                    if c == ")" and top == "(" or c == "}" and top == "{" or c == "]" and top == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return False if stack else True
        