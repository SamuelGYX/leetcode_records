'''
213. House Robber II
Medium

Compute the max sum of subarray without adjacent elements, the first and last element are considered adjacent.

Solution:

    Compute two ordinary rob results.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_(A):
            s1 = s2 = 0
            for a in A:
                s1, s2 = s2, max(s1+a, s2)
            return s2
        if len(nums) == 1:
            return nums[0]
        else:
            return max(rob_(nums[1:]), rob_(nums[:-1]))