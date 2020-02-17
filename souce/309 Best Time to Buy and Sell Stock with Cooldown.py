'''
309. Best Time to Buy and Sell Stock with Cooldown
Medium

Buy and sell any times, but with one day cool down time.

Solution:

	Finite State Machine

	rest			rest
	^v				 ^v
	S0 -----buy----> S1 -----sell----> S2
	^									v
	|									|
	+---------------rest----------------+

	S0 could rest of buy, S1 could rest or sell, S2 could only rest.

	S0: maximum profit at day i after rest (from S0 or S2) at day i
	S1: maximum profit at day i after buy (from S0) or rest (from S1) at day i
	S2: maximum profit at day i after sell (from S1) at day i
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        s0, s1, s2 = 0, -prices[0], 0
        for a in prices:
            s0, s1, s2 = max(s0, s2), max(s0-a, s1), s1+a
        return max(s0, s2)