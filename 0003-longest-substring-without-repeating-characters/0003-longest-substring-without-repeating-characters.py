class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l = 0
        maxLen = 0
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen