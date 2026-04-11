class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        out = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                idx = (ord(c) - ord('a'))
                count[idx] += 1
            d[tuple(count)].append(s)
        return d.values()
