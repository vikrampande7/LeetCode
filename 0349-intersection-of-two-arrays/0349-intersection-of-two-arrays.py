class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset_1 = set(nums1)
        hashset_2 = set(nums2)

        return (list(hashset_1) & list(hashset_2))