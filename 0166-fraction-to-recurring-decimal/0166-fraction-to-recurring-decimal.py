class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = ""
        if (numerator * denominator) < 0:
            res += "-"
        absNum = abs(numerator)
        absDen = abs(denominator)
        intDiv = absNum // absDen
        res += str(intDiv)
        remainder = absNum % absDen
        if remainder == 0:
            return res
        
        res += "."
        mp = {}
        while remainder != 0:
            if remainder in mp:
                insert_pos = mp[remainder]
                res = res[:insert_pos] + "(" + res[insert_pos:] + ")"
                break
            mp[remainder] = len(res)
            remainder *= 10
            digit = remainder // absDen
            res += str(digit)
            remainder %= absDen
        return res

        