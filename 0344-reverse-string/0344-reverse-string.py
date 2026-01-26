class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # def recursion(s, l, r):
        #     if l < r:
        #         s[l], s[r] = s[r], s[l]
        #         recursion(s, l+1, r-1)
        # recursion(s, 0, len(s)-1)
        def rec(s, l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                rec(s, l+1, r-1)
        return rec(s, 0, len(s) - 1)