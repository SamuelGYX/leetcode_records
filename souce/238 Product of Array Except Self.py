'''
238. Product of Array Except Self
Medium

Solution:

    index       0   1   2   3
                1   2   3   4
    left        1   1   2   6
    right       24  12  4   1
    out         24  12  8   6
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1 for _ in range(n)]
        for i in range(1, n):
            out[i] = out[i-1] * nums[i-1]
        r = 1
        for i in reversed(range(n)):
            out[i] *= r
            r *= nums[i]
        return out