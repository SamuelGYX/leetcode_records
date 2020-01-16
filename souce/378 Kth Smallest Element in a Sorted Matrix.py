'''
Overview:

	Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Solution:

	Example:

		matrix = [
		   [ 1,  5,  9],
		   [10, 11, 13],
		   [12, 13, 15]
		],
		k = 8,

		return 13.

	Create one generator for each row of the matrix. Merge these generators with heapq and output the k-th element.
'''

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        streams = map(lambda i: (matrix[i][j] for j in range(len(matrix[0]))), range(len(matrix)))
        stream = heapq.merge(*streams)
        return list(itertools.islice(stream, k-1, k))[0]