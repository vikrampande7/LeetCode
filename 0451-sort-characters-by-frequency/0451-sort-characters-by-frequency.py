class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for c in s:
            hm[c] = hm.get(c, 0) + 1

        sorted_dict_desc = sorted(hm.items(), key=lambda item: item[1], reverse=True)
                
        f = ""
        for i in sorted_dict_desc:
            k, v = i
            f += k * v

        return f