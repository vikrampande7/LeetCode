class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        stack.append(nums[0])
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                hashmap[stack.pop()] = nums[i]
            stack.append(i)
            hashmap[i] = -1
        last_idx = len(nums) - 1
        last_element = nums[-1]
        for i in range(len(nums) - 1):
            if nums[i] > last_element:
                hashmap[last_idx] = nums[i]
        return list(hashmap.values())