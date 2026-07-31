class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        freq = [0] * 26
        for char in word:
            freq[ord(char) - ord("a")] += 1
        freq.sort(reverse=True)
        pushes = 0
        for i in range(26):
            if freq[i] == 0:
                break
            pushes += (i // 8 + 1) * freq[i]
        return pushes