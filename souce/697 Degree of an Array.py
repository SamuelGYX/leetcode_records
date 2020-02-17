'''
697. Degree of an Array
Easy

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements. Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt, first, degree, out = collections.Counter(), {}, 0, 1
        for i, a in enumerate(nums):
            cnt[a] += 1
            first.setdefault(a, i)
            if degree < cnt[a]:
                degree, out = cnt[a], i-first[a]+1
            elif degree == cnt[a]:
                out = min(out, i-first[a]+1)
        return out