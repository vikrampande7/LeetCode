class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Iterate i and i+1 within a loop
        """
        score = 0
        for i in range(len(s)-1):
            score += abs(ord(s[i]) - ord(s[i+1]))
                
        return score