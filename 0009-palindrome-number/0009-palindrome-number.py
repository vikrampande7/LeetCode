class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x[::-1] == str_x
        