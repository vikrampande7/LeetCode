class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space: O(N) and Time O(NlogN)
        # s_sorted = ''.join(sorted(s))
        # t_sorted = ''.join(sorted(t))
        # return s_sorted == t_sorted

        # Space: O(1) Time: O(N+M)
        if len(s) != len(t):
            return False

        hash_s = {}
        hash_t = {}

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

        return hash_s == hash_t


        