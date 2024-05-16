class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''Find difference of target and values in array, add them to hashmap'''
        hashMap = {}
        for i, num in enumerate(nums):
            difference = target - num
            
            if difference in hashMap:
                return [hashMap[difference], i]
            
            hashMap[num] = i
            
            
          
        # BruteForce
        #   for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i, j
        
        
#         num_indices = {}
#         for i, num in enumerate(nums):
#             complement = target - num
            
#             if complement in num_indices:
#                 return [num_indices[complement], i]

#             num_indices[num] = i
        
                
        
        