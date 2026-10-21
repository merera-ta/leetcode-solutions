class Solution(object):
    def twoSum(self, nums, target):
        # Check every number in the array one by one
        for i in range(len(nums)):
            
            # Compare the current number with every number that comes AFTER it
            for j in range(i + 1, len(nums)):
                
                # If they add up to the target, we found our pair
                if nums[i] + nums[j] == target:
                    return [i, j]