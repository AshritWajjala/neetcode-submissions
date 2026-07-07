class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for ind, val in enumerate(nums):
            if ind > 0 and val == nums[ind - 1]:
                continue
            l = ind + 1
            r = len(nums) - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1

                else:
                    result.append([val, nums[l], nums[r]])
                    # If l is not incremented, while loop won't stop
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: # Inorder to skip duplicate values
                        l += 1
        
        return result