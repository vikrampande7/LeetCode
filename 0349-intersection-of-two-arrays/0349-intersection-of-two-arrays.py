class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1=list(set(nums1))
        num2=list(set(nums2))
        common = list(set(num1) & set(num2))
        if common:
             return common
        return []
        