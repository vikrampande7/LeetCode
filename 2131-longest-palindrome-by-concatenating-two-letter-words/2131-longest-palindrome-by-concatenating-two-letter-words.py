from itertools import combinations, permutations
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = {}
        longest = 0

        for word in words:
            r_word = word[::-1]
            if hashmap.get(r_word, 0) > 0:
                longest += 4
                hashmap[r_word] -= 1
            else:
                hashmap[word] = hashmap.get(word, 0) + 1

        for word, count in hashmap.items():
            if word[0] == word[1] and count > 0:
                longest += 2
                break

        return longest





        # Memory Exceeded
        # longest = 0
        # res = []

        # def check_palindrome(s):
        #     i, j = 0, len(s)-1
        #     is_pali = True
        #     while i < j:
        #         if s[i] != s[j]:
        #             is_pali = False
        #             break
        #         i += 1
        #         j -= 1

        #     if is_pali: 
        #         return len(s) 
        #     else: 
        #         return 0

        # for i in range(1, len(words)+1):
        #     for combo in permutations(words, i):
        #         res.append(''.join(combo))

        # for combo in res:
        #     #print(combo)
        #     l = check_palindrome(combo)
        #     longest = max(longest, l)

        # return longest



        