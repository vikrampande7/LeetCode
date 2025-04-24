class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = {}

        count = 0
        maxSize = 0

        def findDigitSum(num):
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num //= 10
            return digitSum
            
        for num in range(1, n+1):
            digitSum = findDigitSum(num)
            hashmap[digitSum] = hashmap.get(digitSum, 0) + 1
            
            if hashmap[digitSum] == maxSize:
                count += 1
            elif hashmap[digitSum] > maxSize:
                maxSize = hashmap[digitSum]
                count = 1
                
        return count


        