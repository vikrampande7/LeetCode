class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        res = []
        if s[0] == "-":
            res.append(s[0])
            s = s[1:]
        print(s)
        for c in s:
            if c == '-':
                res = []
                break
            if c not in "0123456789":
                break
            res.append(c)   
        if not res:
            return 0
        else: 
            return int("".join(res))   
        