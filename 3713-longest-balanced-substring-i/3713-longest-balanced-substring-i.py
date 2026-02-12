class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(len(s)):
            freq = defaultdict(int)
            for j in range(len(s)):
                freq[s[j]] += 1
                if len(set(freq.values())) == 1:
                    res = max(res, j-i+1)
        return res