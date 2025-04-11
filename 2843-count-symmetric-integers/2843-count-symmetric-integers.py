class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high+1):
            if len(str(num)) >= 2 and len(str(num)) % 2 == 0:
                m = int(len(str(num)) / 2)
                numStr = str(num)
                fhs, shs = 0, 0
                
                for fh in numStr[:m]:
                    fhs += int(fh)
                    
                for sh in numStr[m:]:
                    shs += int(sh)
                    
                if fhs == shs:
                    count += 1

        return count

        