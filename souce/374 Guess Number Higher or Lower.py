'''
374. Guess Number Higher or Lower
Easy

I pick a number from 1 to n. You have to guess which number I picked.

Solution:

	The result returned by 'guess(int num)' shall be [1 1 1 0 -1 -1 -1]. We could toggle (negate) the result and apply binary search to find the index of 0.
'''

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        class C: __getitem__ = lambda _, i: -guess(i)
        return bisect.bisect_left(C(), 0, 1, n+1)