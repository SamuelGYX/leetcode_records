'''
714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

Buy and sell any times with transaction fee.

Solution:

	Finite State Machine
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        b, s = -math.inf, 0
        for a in prices:
            b, s = max(b, s-a-fee), max(s, b+a)
        return s