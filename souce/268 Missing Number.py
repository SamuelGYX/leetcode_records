'''
268. Missing Number
Easy

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Time = O(n), Space = O(1)

Solution:

	1. XOR

	2. expect_sum - actual_sum

	3. mark the numbers stored in index i when we find number i in the array

		3.1 negative sign

			Not applicable because there may be number 0 in the array. Negative zero is the same as positive zero. We could resolve this by mark 0 as 'special_char' but it needs more branches.

		3.2 (nums[i]%n) += n

			We need to append one dummy value before applying this method in order to make the length of array to be n+1, which maps [0,n] to be [n+1,2n+1] without intersection.

		3.3 swap number i into index i
'''

class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i, v in enumerate(nums):
            ans ^= i ^ v
        return ans

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp_sum, act_sum = n * (n+1) // 2, sum(nums)
        return exp_sum - act_sum

class Solution3_2:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(nums[0])
        n = len(nums)
        for i, v in enumerate(nums):
            nums[v%n] += n
        for i, v in enumerate(nums):
            if v < n:
                return i

class Solution3_3:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        for i, v in enumerate(nums):
            while i != v and v != -1:
                nums[i], nums[v], v = nums[v], nums[i], nums[v]
        for i, v in enumerate(nums):
            if i != v:
                return i