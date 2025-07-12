class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        out = ""
        for w in range(len(words)-1, -1, -1):
            print(words[w])
            out += words[w] + ' '
        out = out.strip()
        return out

        