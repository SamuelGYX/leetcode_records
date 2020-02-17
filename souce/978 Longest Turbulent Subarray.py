'''
978. Longest Turbulent Subarray
Medium

Turbulent means A[i-1] < A[i] > A[i+1] or A[i-1] > A[i] < A[i+1]

Solution:

    Solution 1:

        Hard code all situations.

                A[i-1]>A[i]     A[i-1]<A[i]     ==
        odd     len1+1, 1       1, len2+1       1, 1
        even    1, len2+1       len1+1, 1       1, 1

    Solution 2:

        Swap len1 and len2.

                A[i-1]>A[i]     A[i-1]<A[i]     ==
                1, inc+1        dec+1, 1        1, 1

Example:

            [9,4,2,10,7,8,8,1,9]

    index   0   1   2   3   4   5   6   7   8
    len1    1   2   1   1   1   1   1   2   3
    len2    1   1   2   3   4   5   1   1   1
    inc     1   1   1   3   1   5   1   1   3
    dec     1   2   2   1   4   1   1   2   1
'''

class Solution1:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        out = len1 = len2 = 1
        for i in range(1, len(A)):
            len1 = len1+1 if (i%2 and A[i-1]>A[i] or not i%2 and A[i-1]<A[i]) else 1
            len2 = len2+1 if (not i%2 and A[i-1]>A[i] or i%2 and A[i-1]<A[i]) else 1
            out = max(out, len1, len2)
        return out

class Solution2:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        out = inc = dec = 1
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                inc, dec = dec + 1, 1
            elif A[i-1] > A[i]:
                inc, dec = 1, inc + 1
            else:
                inc, dec = 1, 1
            out = max(out, inc, dec)
        return out