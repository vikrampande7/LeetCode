class TwoSum:

    def __init__(self):
        self.array = []

    def add(self, number: int) -> None:
        self.array.append(number)

    def find(self, value: int) -> bool:
        hashmap = {}
        for index, num in enumerate(self.array):
            if value - num in hashmap:
                return True
            hashmap[num] = index
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)