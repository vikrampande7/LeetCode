class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l = 0
        longest = 0
        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l])
                l += 1
            visit.add(s[r])
            longest = max(longest, r - l + 1)
        return longest