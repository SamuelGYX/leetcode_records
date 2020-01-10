'''
Overview:

    Write a program to find the nth super ugly number.

    Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Solution:

    sol_1: O(nlgk)

        1. genUgly(prime): a generator (list)
        e.g.    [u0*p u1*p ...]

        2. map(genUgly, primes): a generator (list) of generator (list)
        e.g.    [
                    [u0*p0 u1*p0 ...]
                    [u0*p1 u1*p1 ...]
                    ...
                ]

        3. *map(genUgly, primes): feed all elements in a list as arguments
        e.g.    [u0*p0 u1*p0 ...]
                [u0*p1 u1*p1 ...]
                ...
            This is because
            lists = [[1, 3, 5], [2, 4, 6]]
            list(heapq.merge(lists))        # [[1, 3, 5], [2, 4, 6]]
            list(heapq.merge(*lists))       # [1, 2, 3, 4, 5, 6]
            i.e. 
                merge could accept one argument or multiple arguments. The element in an argument is the element for merging.

        4. heapq.merge(*map(genUgly, primes)): a generator (list) in ascending order
        e.g.    [u0*p0 u0*p1 u0*p2 u1*p0 ...]

        Keep in mind: variables in a generator function could be updated in runtime. Actually, the original uglyGen only contains k elements because u1 does not exist in the beginning.

    sol_2: O(nk)

        Extension from "264 Ugly Number II".
'''

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1]
        def genUgly(prime):
            for u in ugly:
                yield u * prime
        uglyGen = heapq.merge(*map(genUgly, primes))
        while len(ugly) < n:
            nxt = next(uglyGen)
            if nxt != ugly[-1]:
                ugly.append(nxt)
        return ugly[-1]

class Solution2:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1 for _ in range(n)]
        a = [0 for _ in range(len(primes))]
        for i in range(1, n):
            c = [ugly[x]*y for x,y in zip(a, primes)]
            ugly[i] = min(c)
            for j in range(len(primes)):
                if ugly[i] == c[j]:
                    a[j] += 1
        return ugly[-1]