class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "1":
            return None
        if not digits:
            return None
        
        phone_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        
        def tracking(idx, combi):
            if idx == len(digits):
                res.append(combi)
                return
            
            curr = digits[idx]
            for letter in phone_map[curr]:
                tracking(idx+1, combi+letter)
                
        tracking(0, "")
    
        return res
            
        
        