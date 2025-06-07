class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        minCharToRight = n * [0] # Right to Left Traversal
        minCharToRight[n-1] = s[n-1]
        for i in range(n-2, -1, -1):
            minCharToRight[i] = min(s[i], minCharToRight[i+1])
        
        i = 0
        t = ""
        p = ""

        while i < n:
            t += s[i]
            if i+1<n:
                minChar = minCharToRight[i+1]
            else:
                minChar = s[i]

            while t and t[-1] <= minChar:
                p += t[-1]
                t = t[:-1]

            i += 1

        while t:
            p += t[-1]
            t = t[:-1]

        return p