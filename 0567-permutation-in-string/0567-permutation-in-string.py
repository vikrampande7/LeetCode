class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sorting Approach
        # n = len(s1)
        # m = len(s2)

        # if n == m:
        #     if s1==s2:
        #         return True
        # elif n > m:
        #     return False

        # s1 = sorted(s1)

        # for i in range(0, m-1):
        #     sbstr = s2[i:i+n]
        #     if sorted(sbstr) == s1:
        #         return True
        
        # return False

        # Sliding Window + Character Count Approach
        n = len(s1)
        m = len(s2)
        
        s1_freq, s2_freq = 26*[0], 26*[0]

        for char in s1:
            s1_freq[ord(char) - ord('a')] += 1

        l = 0
        for r in range(m):
            current_char = ord(s2[r]) - ord('a')
            s2_freq[current_char] += 1

            if r - l + 1 > n:
                left_char = ord(s2[l]) - ord('a')
                s2_freq[left_char] -= 1
                l+= 1

            if r-l+1 ==n and s1_freq == s2_freq:
                return True

        return False