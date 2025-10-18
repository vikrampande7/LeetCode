class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        charLen = {}
        maxLen = 0
        for i, s in enumerate(strs):
            charLen[s] = len(s)
            maxLen = max(len(s), maxLen)

        for k, v in charLen.items():
            if v == maxLen:
                word = k

        for i in range(maxLen):
            for s in strs:
                if i == len(s) or s[i] != word[i]:
                    return longest
            longest += word[i]
        
        return longest