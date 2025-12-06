class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.hashmap = {}
        for word in dictionary:
            if len(word) == 2:
                if word not in self.hashmap:
                    self.hashmap[word] = 1
                self.hashmap[word] += 1
            if len(word) > 2:
                firstChar, lastChar = word[0], word[-1]
                charsBetween = str(len(word) - 2)
                abbr = f"{firstChar}{charsBetween}{lastChar}"
                if abbr not in self.hashmap:
                    self.hashmap[abbr] = 1
                else:
                    self.hashmap[abbr] += 1
        print(self.hashmap)

    def isUnique(self, word: str) -> bool:
        if len(word) == 2:
                if word not in self.hashmap:
                    return True
                else:
                    if self.hashmap[word] >= 1:
                        return False
                    else:
                        return True
        if len(word) > 2:
            firstChar, lastChar = word[0], word[-1]
            charsBetween = str(len(word) - 2)
            abbr = f"{firstChar}{charsBetween}{lastChar}"
            if abbr not in self.hashmap:
                return True
            else:
                if self.hashmap[abbr] >= 1:
                        return False
                else:
                    return True
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)