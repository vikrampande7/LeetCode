class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list)
        for s in strs:
            anagrams = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                anagrams[idx] += 1
            ans[tuple(anagrams)].append(s)
        return [v for k, v in ans.items()]