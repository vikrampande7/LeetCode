class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        curr = []

        def is_palindrome(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        def recursion(start):
            if start == len(s):
                out.append(curr[:])
                return

            for end in range(start+1, len(s)+1):
                substring = s[start:end]

                if is_palindrome(substring):
                    curr.append(substring)
                    recursion(end)
                    curr.pop()

        recursion(0)
        return out


        