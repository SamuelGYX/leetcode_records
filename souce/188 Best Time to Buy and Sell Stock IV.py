'''
188. Best Time to Buy and Sell Stock IV
Hard

Buy and sell at most k times.

Solution:

	Finite State Machine
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k*2 >= len(prices):
            return sum(prices[i]-prices[i-1] for i in range(1,len(prices)) if prices[i]>prices[i-1])
        S = [0] + [-math.inf for _ in range(k*2)]
        for a in prices:
            S = [0] + [max(S[i], S[i-1]+a*(-1)**i) for i in range(1, len(S))]
        return max(S)