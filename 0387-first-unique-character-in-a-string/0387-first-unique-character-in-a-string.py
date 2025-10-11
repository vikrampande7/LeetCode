class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        unique = []
        for k, v in hashmap.items():
            if v == 1:
                unique.append(k)
        min_idx = float("inf")
        for i, c in enumerate(s):
            if c in unique:
                min_idx = min(min_idx, i)
        return min_idx if min_idx != float("inf") else -1
        