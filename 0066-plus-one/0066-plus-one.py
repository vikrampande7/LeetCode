class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        out = []
        for num in digits:
            n += str(num)
        n = str(int(n) + 1)
        for d in n:
            out.append(int(d))
        
        return out