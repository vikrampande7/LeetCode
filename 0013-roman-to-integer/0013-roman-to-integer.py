class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        total = 0
        i = 0
        n = len(s)
        while i < n:
            if i < n - 1 and s[i:i+2] in mp:
                total += values[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total