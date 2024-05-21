class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower = 1
        upper = num
        
        while lower <= upper:
            m = (lower + upper) // 2
            if m*m == num:
                return True
            elif m*m >num:
                upper = m - 1
            else:
                lower = m + 1
                
        return False
        