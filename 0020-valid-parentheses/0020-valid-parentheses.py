class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closing = 0
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                closing += 1
            if stack:
                top = stack[-1]
                if top == "(" and c == ')':
                    stack.pop()
                    closing -= 1
                if top == "[" and c == ']':
                    stack.pop()
                    closing -= 1
                if top == "{" and c == '}':
                    stack.pop()
                    closing -= 1
        return True if (len(stack) == 0 and closing == 0) else False