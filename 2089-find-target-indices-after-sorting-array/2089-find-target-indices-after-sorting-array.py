class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []

        # for i in range(0, len(nums)):
        #     if nums[i] == target:
        #         indices.append(i)

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                for i in range(mid,l-1,-1): 
                    if nums[i] == target:
                        indices.append(i)
                    else:
                        break
                for i in range(mid+1,r+1): 
                    if nums[i] == target:
                        indices.append(i)
                    else:
                        break
                return sorted(indices)
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return indices
        