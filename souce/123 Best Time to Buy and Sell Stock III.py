'''
123. Best Time to Buy and Sell Stock III
Hard

Buy and sell at most twice.

Solution:

	Finite State Machine
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        b1, s1, b2, s2 = -math.inf, 0, -math.inf, 0
        for a in prices:
            b1, s1, b2, s2 = max(b1, -a), max(s1, b1+a), max(b2, s1-a), max(s2, b2+a)
        return s2