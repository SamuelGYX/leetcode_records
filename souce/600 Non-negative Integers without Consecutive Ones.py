'''
600. Non-negative Integers without Consecutive Ones
Hard

Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Solution:

    First, find all candidate strings without consecutive ones with length n.

        one[i]: number of good strings with '1' at i-th bit (start from 0)
        zero[i]: number of good strings with '0' at i-th bit

                            zero[i+1]   one[i+1]
        zero[i] 0...    =>  00...    or 10...
        one[i]  1...    =>  01...

        Thus, 

        zero[i+1] = zero[i] + one[i]
        one[i+1] = zero[i]

    Second, subtract from result all numbers larger than num.

        loop invariant: cand[0:i] ≤ num[0:i], i.e. bad bit of all candidates starts from i, all previous bits of all candidates are no larger than num.
'''

class Solution:
    def findIntegers(self, num: int) -> int:
        s = format(num, 'b')
        n = len(s)
        one, zero = [1 for _ in range(n)], [1 for _ in range(n)]
        for i in range(1, n):
            one[i], zero[i] = zero[i-1], one[i-1] + zero[i-1]
        out = one[n-1] + zero[n-1]
        for i in range(1, n):
            if s[i-1] == '1' and s[i] == '1':
                break
            elif s[i-1] == '0' and s[i] == '0':
                out -= one[n-1-i]
        return out