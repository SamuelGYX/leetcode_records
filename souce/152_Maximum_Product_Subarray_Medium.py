'''
Overview:

	Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Solution:

	Enhanced DP:

		dp_i is used to record 2 values: min and max product end with i

		dp_i_min = min(dp_i-1_min * num_i, num_i)
		dp_i_max = max(dp_i-1_max * num_i, num_i)

	This is because multiply with negative number will exchange the value of min and max.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = dp_min = dp_max = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dp_min, dp_max = dp_max, dp_min
            
            dp_min = min(dp_min * nums[i], nums[i])
            dp_max = max(dp_max * nums[i], nums[i])
            
            res = max(res, dp_max)
            
        return res