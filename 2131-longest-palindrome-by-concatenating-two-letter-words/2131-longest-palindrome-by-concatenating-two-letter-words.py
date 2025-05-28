from itertools import combinations, permutations
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        longest = 0
        res = []

        def check_palindrome(s):
            i, j = 0, len(s)-1
            is_pali = True
            while i < j:
                if s[i] != s[j]:
                    is_pali = False
                    break
                i += 1
                j -= 1

            if is_pali: 
                return len(s) 
            else: 
                return 0

        for i in range(1, len(words)+1):
            for combo in permutations(words, i):
                res.append(''.join(combo))

        for combo in res:
            #print(combo)
            l = check_palindrome(combo)
            longest = max(longest, l)

        return longest



        