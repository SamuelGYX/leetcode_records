'''
Overview:

    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Solution:

    > The ith order statistic of a set of n elements is the ith smallest element. 

    -- from Introduction to Algorithms

    Recursive select with randomized partition extracted from the above book.
'''

from random import randint

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums)-1, len(nums)+1-k)
        
    def select(self, nums, p, r, i):
        # print(p, r, k)
        if p == r:
            return nums[p]
        pivot = self.partition(nums, p, r)
        k = pivot - p + 1
        if i < k:
            return self.select(nums, p, pivot-1, i)
        elif i > k:
            return self.select(nums, pivot+1, r, i-k)
        else:
            return nums[pivot]
        
    def partition(self, nums, p, r):
        i = randint(p, r)
        nums[i], nums[r] = nums[r], nums[i]
        i = p - 1
        for j in range(p, r):
            if nums[j] <= nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1