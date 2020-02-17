'''
198. House Robber
Easy

Compute the max sum of subarray without adjacent elements.

Solution:
	
	rob(i) = max(rob(i-1), rob(i-2)+nums[i])

	We use s1, s2 to denote rob(i-2), rob(i-1).
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        s1, s2 = 0, 0
        for a in nums:
            s1, s2 = s2, max(s1+a, s2) 
        return s2