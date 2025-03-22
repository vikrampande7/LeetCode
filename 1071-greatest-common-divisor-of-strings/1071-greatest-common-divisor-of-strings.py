class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        for i in range(0, len(str1), len(str2)):
            if str2 == str1[i:i+len(str2)]:
                str1 = str1.replace(str2,"",1)
                return str1
            else:
                return ""

        