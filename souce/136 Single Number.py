'''
136. Single Number
Easy

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Time: O(n), Space: O(1)
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans