class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        
    def add(self, index: int, val: int) -> None:
        self.nums2[index] = self.nums2[index] + val
        
    def count(self, tot: int) -> int:
        if len(self.nums1) < len(self.nums2):
            padding_length = len(self.nums2) - len(self.nums1)
            self.nums1 += [0] * padding_length
        elif len(self.nums1) > len(self.nums2):
            padding_length = len(self.nums1) - len(self.nums2)
            self.nums2 += [0] * padding_length

        count = 0
        for i in range(len(self.nums1)):
            for j in range(len(self.nums1)):
                if self.nums1[i] + self.nums2[j] == tot:
                    count += 1
        return count
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)