class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = [-1] * len(nums1)
        # for i, num1 in enumerate(nums1):
        #     found = False
        #     for j, num2 in enumerate(nums2):
        #         if found and num2 > num1:
        #             res[i] = num2
        #             break
        #         if num2 == num1:
        #             found = True
        # return res

        ## Monotonous Stack
        stack = []
        hashmap = {}
        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                res[i] = hashmap[nums1[i]]
        return res



        