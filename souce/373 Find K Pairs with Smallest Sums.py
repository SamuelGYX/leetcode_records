'''
Overview:

	You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

	Define a pair (u,v) which consists of one element from the first array and one element from the second array.

	Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Solution:

	nums1: [1,7,11]
	nums2: [2,4,6]

	      2   4   6
	   +------------
	 1 |  3   5   7
	 7 |  9  11  13
	11 | 13  15  17

	Streams is a list contains a generator for each row. Merge combines all 3 rows to get the smallest one.

Tricky point:

	`()` means generator; `[]` means list.
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        streams = map(lambda i: ([i+j, i, j] for j in nums2), nums1)
        stream = heapq.merge(*streams)
        return [out[1:] for out in itertools.islice(stream, k)]