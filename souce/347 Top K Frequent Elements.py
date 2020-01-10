'''
Overview:

	Given a non-empty array of integers, return the k most frequent elements.

Solution:

	Counter function and heapq (or sorted)
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)