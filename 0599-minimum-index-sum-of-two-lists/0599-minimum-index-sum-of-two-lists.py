class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = defaultdict(list)
        for i, s in enumerate(list1):
            if s in list2:
                hashmap[s].append(i)
        for i, s in enumerate(list2):
            if s in list1:
                hashmap[s].append(i)
        minSum = float("inf")
        for key, value in hashmap.items():
            minSum = min(minSum, sum(value))
        out = []
        for key, value in hashmap.items():
            if sum(value) == minSum:
                out.append(key)
        return out