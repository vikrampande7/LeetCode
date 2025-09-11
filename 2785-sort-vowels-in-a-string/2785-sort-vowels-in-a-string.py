class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v = []
        s_l = list(s)
        for i, c in enumerate(s_l):
            if c in vowels:
                s_l[i] = '*'
                v.append(ord(c))
        v.sort()
        
        idx = 0
        for i, c in enumerate(s_l):
            if s_l[i] == '*':
                s_l[i] = chr(v[idx])
                idx += 1      
        t = ""
        for c in s_l:
            t += c
        return t