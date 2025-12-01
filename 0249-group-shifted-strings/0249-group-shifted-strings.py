class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = []
        hashmap = defaultdict(list)
        for word in strings:
            pattern = []
            for i in range(len(word)-1):
                diff = (ord(word[i+1]) - ord(word[i])) % 26
                pattern.append(diff)
            hashmap[tuple(pattern)].append(word)
        for key, value in hashmap.items():
            res.append(value)
        return res