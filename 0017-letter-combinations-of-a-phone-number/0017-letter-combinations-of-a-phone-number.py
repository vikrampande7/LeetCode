class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digitsToChars = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        res = []
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            for eachChar in digitsToChars[digits[i]]:
                backtrack(i+1, currStr+eachChar)
        backtrack(0, "")
        return res