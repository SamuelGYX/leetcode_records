'''
628. Maximum Product of Three Numbers
Easy

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Solution:

	max_product = max(top[0]*top[1]*top[2], top[0]*bottom[0]*bottom[1])
'''

import functools
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        top, bot = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return top[0] * max(functools.reduce(operator.mul, top[1:]), functools.reduce(operator.mul, bot))