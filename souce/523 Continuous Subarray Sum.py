'''
523. Continuous Subarray Sum
Medium

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

Solution:

    [23,2,6,4,7] => running sum: [23,25,31,35,42] => mod 6: [5,1,1,5,0]

    We have summed multiples of k between two identical mod results (i.e. [index 0 and 3] and [index 2 and 3]).

    Tricky points:

        1. ind is initialized with {0: -1} to handle the case where the whole list summed up to multiple of k

        2. when k == 0, we cannot mod the sum

        3. it is required that the length of the subarray is at least 2

        4. if ind[s] exist, we cannot update it because we need to record the farthest begin index, in order to fulfill the length requirement

        5. [0, 0] subarray could fulfill any k because 0 is 0*k. Therefore, [23, 0, 0, 0, 0] returns True.
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ind, s = {0: -1}, 0
        for i, v in enumerate(nums):
            s = (s + v) % k if k else s + v
            if s in ind:
                if i - ind[s] >= 2:
                    return True
            else:
                ind[s] = i
        return False