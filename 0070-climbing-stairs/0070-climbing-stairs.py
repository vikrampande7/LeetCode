class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        second_last = 1
        
        for i in range(n-1):
            updated_last = second_last
            second_last = second_last + last
            last = updated_last

        return second_last


