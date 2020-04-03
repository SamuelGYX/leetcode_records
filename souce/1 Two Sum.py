'''
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i, v in enumerate(nums):
            if target-v in ind:
                return [ind[target-v], i]
            else:
                ind[v] = i