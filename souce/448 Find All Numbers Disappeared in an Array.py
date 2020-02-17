'''
448. Find All Numbers Disappeared in an Array
Easy

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once. Find all the elements of [1, n] inclusive that do not appear in this array.

Time = O(n), Space = O(1)

Solution:

	Special mark

	1. Negative sign

	2. +n

	3. Swap

'''

class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, v in enumerate(nums):
            nums[abs(v)-1] = -abs(nums[abs(v)-1])
        return [i+1 for i, v in enumerate(nums) if v > 0]

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, v in enumerate(nums):
            nums[(v-1)%n] += n
        return [i+1 for i, v in enumerate(nums) if v <= n]

class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, v in enumerate(nums):
            while i != v-1 and v != nums[v-1]:
                nums[i], nums[v-1], v = nums[v-1], nums[i], nums[v-1]
        return [i+1 for i, v in enumerate(nums) if i != v-1]