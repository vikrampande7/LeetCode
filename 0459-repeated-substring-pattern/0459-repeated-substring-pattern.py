class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0: # Create substrings of length divisible by length of original string
                sub = s[:i] * (n // i) # to match the length of original string
                if sub == s:
                    return True
        return False
        