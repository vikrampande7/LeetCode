class Solution:
    def myAtoi(self, s: str) -> int:
        # s = s.lstrip()
        # res = []
        # if s[0] == "-":
        #     res.append(s[0])
        #     s = s[1:]
        # print(s)
        # for c in s:
        #     if c == '-':
        #         res = []
        #         break
        #     if c not in "0123456789":
        #         break
        #     res.append(c)   
        # if not res:
        #     return 0
        # else: 
        #     return int("".join(res))   
        
        sign = 1
        res = 0
        idx = 0
        n = len(s)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        while idx < n and s[idx] == " ":
            idx += 1

        if idx < n and (s[idx] == '+' or s[idx] == '-'):
            sign = -1 if s[idx] == '-' else 1
            idx += 1

        while idx < n and s[idx].isdigit():
            digit = int(s[idx])
            if (res > INT_MAX // 10) or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            res = 10 * res + digit
            idx += 1

        return sign * res