### Max profit
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        curr_buy = prices[0] + fee
        tot = 0
        for i in range(1, len(prices)):
            if prices[i] + fee < curr_buy:
                curr_buy = prices[i] + fee
            if prices[i] > curr_buy:
                tot += prices[i] - curr_buy
                curr_buy = prices[i]
        return tot        
