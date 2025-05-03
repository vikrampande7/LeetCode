class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in "+-*/":
                first, second = stack[-1], stack[-2]
                if char == '+': res = second + first
                if char == '-': res = second - first
                if char == '*': res = second * first
                if char == '/': res = int(second / first)
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(char))

        return stack[-1]

        