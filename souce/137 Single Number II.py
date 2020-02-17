'''
137. Single Number II
Medium

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Time: O(n), Space: O(1)

Solution:

> https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

	1. 2 counters for 3 duplication

		k = 3 (11 in binary) means we need 2 bits to count the common elements.

	2. Generalized method for any k, p
'''
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        x1, x2 = 0, 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x2 & x1)
            x2 &= mask
            x1 &= mask
        return x1

import functools
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        k, p, m = 3, 1, math.ceil(math.log2(3))
        x, b = [0 for _ in range(m)], [k&(1<<r) for r in range(m)]
        for i in nums:
            temp_and = list(itertools.accumulate([i] + x, operator.and_))
            x = [xi ^ ai for xi, ai in zip(x, temp_and)]
            mask = ~functools.reduce(operator.and_, [xi if bi else ~xi for xi, bi in zip(x, b)])
            x = [xi & mask for xi in x]
        return functools.reduce(operator.or_, x)