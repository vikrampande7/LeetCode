class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = defaultdict(list) # {key (26 chars): [words]}
        for word in strs:
            anagrams = 26 * [0]
            for c in word:
                idx = ord(c) - ord('a')
                anagrams[idx] += 1
            ans[tuple(anagrams)].append(word)
        return [v for k, v in ans.items()]