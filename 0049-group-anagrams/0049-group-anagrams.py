class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            freqCounter = [0] * 26
            for c in word:
                freqCounter[ord(c) - ord('a')] += 1
            res[tuple(freqCounter)].append(word)
        return list(res.values())
        