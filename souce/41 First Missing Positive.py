'''
41. First Missing Positive
Hard

Given an unsorted integer array, find the smallest missing positive integer.

Solution:

    Special mark

    1. Negative sign

        Not applicable because the existence of value 0.

    2. += n

        First, there must be a hole in the range [1, n+1] with n numbers, which means e want to test the existence of numbers in [1, n+1]. Also, the smallest number could be zeros, which indicates the values are in range [0, n+1]. Therefore, We need to make n' = n+2 in order to eliminate intersection.

    3. Swap
'''

class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums += [0, 0]
        n = len(nums)
        for i, v in enumerate(nums):
            if v >= n or v < 0:
                nums[i] = 0
        for i, v in enumerate(nums):
            nums[v%n] += n
        for i, v in enumerate(nums):
            if v < n:
                return i

class Solution3:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums += [0, 0]
        n = len(nums)
        for i, v in enumerate(nums):
            while v >= 0 and v < n and v != nums[v]:
                nums[i], nums[v], v = nums[v], nums[i], nums[v]
        for i, v in enumerate(nums):
            if i != v:
                return i