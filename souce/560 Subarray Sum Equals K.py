'''
560. Subarray Sum Equals K
Medium

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Solution:

	Use cnt to record the occurrences of sum(nums[:i])
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, out, s = collections.Counter([0]), 0, 0
        for v in nums:
            s += v
            out += cnt[s-k]
            cnt[s] += 1
        return out