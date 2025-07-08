class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_m = {}
        t_m = {}
        s_l = []
        t_l = []

        for c in s:
            s_m[c] = s_m.get(c, 0) + 1

        for c in t:
            t_m[c] = t_m.get(c, 0) + 1

        for k, v in s_m.items():
            s_l.append(v)

        for k, v in t_m.items():
            t_l.append(v)

        print(s_l)
        print(t_l)
        return s_l.sort() == t_l.sort()     