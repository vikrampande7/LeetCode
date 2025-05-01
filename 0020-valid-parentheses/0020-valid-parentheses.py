class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        for char in s: #O(n)
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if char == ")" and top == "(" or char == "]" and top == "[" or char == "}" and top == "{":
                    stack.pop() #O(1)
                else:
                    return False
        if not stack:
            return True
        