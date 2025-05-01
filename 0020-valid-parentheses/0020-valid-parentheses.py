class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
            }
        for c in s:
            if c in mapping:
                if stack:
                    if stack[-1] == mapping[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(c)
                
        if not stack:
            return True
        else:
            return False

        # paraDict = {
        # "(":")",
        # "[":"]",
        # "{":"}"
        # }
    
        # stack = []
        # for c in s:
        #     if c not in stack:
        #         stack.append(c)
        #         if len(stack) == 2:
        #             popped = stack.pop()
        #             if paraDict[stack[0]] == popped:
        #                 stack.pop()
        #                 continue
        #             else:
        #                 return False
                    
        # return True if not stack else False
        