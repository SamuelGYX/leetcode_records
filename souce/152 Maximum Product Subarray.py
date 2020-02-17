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

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = max_ = out = nums[0]
        for a in nums[1:]:
            if a < 0:
                min_, max_ = max_, min_
            min_, max_ = min(a, min_*a), max(a, max_*a)
            out = max(max_, out)
        return out