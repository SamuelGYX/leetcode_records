'''
Overview:

    Given an array of 0, 1, and 2. Return the sorted one.

Solution:

    A special sort algorithm for elements with 3 types. Keep a reference to the begin and end location of unsorted area (i.e. area of 1) and scan the unsorted part. If the number is 0 or 2, do swap.

Tricky point:

    Do not increase i when nums[i] == 2 because we do not know what is the new value of nums[i] (i.e. old nums[r]) after swapping.
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, r, i = -1, len(nums), 0
        while i < r:
            if nums[i] == 0:
                p += 1
                nums[p], nums[i] = nums[i], nums[p]
                i += 1
            elif nums[i] == 2:
                r -= 1
                nums[r], nums[i] = nums[i], nums[r]
            else:
                i += 1