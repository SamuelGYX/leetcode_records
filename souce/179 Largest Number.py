'''
Overview:

	Given a list of non negative integers, arrange them such that they form the largest number.

Solution:

	Sort the list with special relationships between two entries.
	Example:
		input list: [3,30,34,5,9]
		output list: [9,5,34,3,30]
'''

class myKey(str):
    def __lt__(self, other):
        return self+other < other+self

class Solution:
    def largestNumber(self, nums):
        res = ''.join(sorted(map(str, nums), key=myKey, reverse=True))
        return '0' if res[0] == '0' else res