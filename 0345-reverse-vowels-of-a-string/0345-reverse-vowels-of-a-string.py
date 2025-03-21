class Solution:
    def reverseVowels(self, s: str) -> str:

        vlist = {'a','e','i','o','u','A','E','I','O','U'}
        vowels_reversed = []
        counter = 0
        s_list = list(s)

        for c in range(len(s)-1,-1,-1):
            if s[c] in vlist:
                vowels_reversed.append(s[c])

        for c in range(0, len(s_list)):
            if s_list[c] in vlist:
                s_list[c] = vowels_reversed[counter]
                counter += 1

        return "".join(s_list)