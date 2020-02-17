'''
1072. Flip Columns For Maximum Number of Equal Rows
Medium

Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

Solution:

	Find the 'pattern' of one row. Return the maximum count of same patterns.

	pattern:

		whether a coin is same as the first coin of its row.

		e.g. [0 0 0] => [1 1 1], [1 0 0] => [1 0 0], [0 1 1] => [1 0 0]

		Same pattern indicates two rows have exactly the same or opposite combinations. This means they will have all same coins after certain flips, i.e. advocates of the same flipping way.
'''

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = (tuple(e ^ r[0] for e in r) for r in matrix)
        cnter = collections.Counter(patterns)
        return max(cnter.values())