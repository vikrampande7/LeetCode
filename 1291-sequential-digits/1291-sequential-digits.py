class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        pattern = "123456789"
        n = 10
        nums = []
        for i in range(len(str(low)), len(str(high))+1):
            for j in range(n - i):
                num = int(pattern[j: j+i])
                if num >= low and num <= high:
                    nums.append(num)
        return nums