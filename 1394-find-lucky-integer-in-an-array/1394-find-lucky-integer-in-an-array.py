class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        fin = []

        for a in arr:
            hashmap[a] = hashmap.get(a, 0) + 1

        for i in hashmap.items():
            if i[0] == i[1]:
                fin.append(i[0])

        fin.sort()

        return fin[-1] if fin else -1
        