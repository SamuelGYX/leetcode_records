'''
167. Two Sum II - Input array is sorted
Easy

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        s = numbers[l] + numbers[r]
        while s != target:
            if s < target:
                l += 1
            else:
                r -= 1
            s = numbers[l] + numbers[r]
        return [l+1, r+1]