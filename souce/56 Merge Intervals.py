'''
Overview:

	Given a collection of intervals, merge all overlapping intervals.

Tricky point:

	>>> l = [1 2 3]
	>>> l.append(l)
	[1 2 3 [1 2 3]]

	>>> l = [1 2 3]
	>>> l.extend(l)
	[1 2 3 1 2 3]

	>>> l = [1 2 3]
	>>> l += l
	[1 2 3 1 2 3]
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        out = []
        for i in sorted(intervals, key=lambda _: _[0]):
            if out and out[-1][1] >= i[0]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out