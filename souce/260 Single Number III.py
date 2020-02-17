'''
260. Single Number III
Medium

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Time: O(n), Space: O(1)

Solution:

	There must be at least one bit difference between ans1 and ans2. We could split the original list into two groups according any bit difference between ans1 and ans2. Then xoring each group yields the final answer.
'''

import functools
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = functools.reduce(operator.xor, nums)
        diff &= -diff
        ans1 = functools.reduce(operator.xor, (i for i in nums if not diff & i))
        ans2 = functools.reduce(operator.xor, (i for i in nums if diff & i))
        return [ans1, ans2]