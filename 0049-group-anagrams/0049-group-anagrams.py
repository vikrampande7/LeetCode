class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time Complexity: O(M*N) -> Neetcode
        anagram_group = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord("a")] += 1
            anagram_group[tuple(count)].append(word) 

        return list(anagram_group.values())
        
        