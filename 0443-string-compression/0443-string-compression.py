class Solution:
    def compress(self, chars: List[str]) -> int:
        insertPos = 0
        i = 0
        while i < len(chars):
            group = 1
            while (group + i) < len(chars) and chars[i] == chars[group + i]:
                group += 1
            chars[insertPos] = chars[i]
            insertPos += 1
            if group > 1:
                charString = str(group)
                chars[insertPos:insertPos+len(charString)] = list(charString)
                insertPos += len(charString)
            i += group
        return insertPos