'''
121. Best Time to Buy and Sell Stock
Easy

Buy and sell stock only once at most. Compute the maximum profit.

Solution:

	Maximum subarray problem.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out, cursum = 0, 0
        for i in range(1, len(prices)):
            cursum = max(cursum+prices[i]-prices[i-1], prices[i]-prices[i-1])
            out = max(out, cursum)
        return out