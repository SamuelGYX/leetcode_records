'''
Overview:

    Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Solution:

    > An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

    Starting from the first ugly number 1, every ugly number U could be used to produce 3 larger ugly numbers: 2*U, 3*U, 5*U.

        u0,     u1,     u2, u3, ...
    2   2*u0    2*u1    ...
    3   3*u0    3*u1    ...
    5   5*u0    5*u1    ...

    The problem is how to produce ugly numbers in order. This could be resolved by keeping 3 separate loop indexes a2, a3, a5, meaning up to which number is the next ugly produced by combination with corresponding b. Then we could get the sequence by picking the smallest result.
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1 for _ in range(n)]
        a, b = [0 for _ in range(3)], [2, 3, 5]
        for i in range(1, n):
            c = [ugly[x]*y for x,y in zip(a, b)]
            ugly[i] = min(c)
            for j in range(3):
                if ugly[i] == c[j]:
                    a[j] += 1
        return ugly[-1]