import sys
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        return self.calculateProfit(prices, 0, 0, False, cache)

    def calculateProfit(self, prices, day, profit, bought, cache) -> int:
        if day >= len(prices):
            return profit
        
        # CHANGE: add profit when returning from cache
        if (day, bought) in cache:
            return profit + cache[(day, bought)]
        
        buy = -sys.maxsize
        if not bought:
            # CHANGE: pass cache in recursive call (was missing before)
            buy = self.calculateProfit(prices, day + 1, profit - prices[day], True, cache)

        sell = -sys.maxsize
        if bought:
            # CHANGE: after selling, bought should become False (cooldown state)
            sell = self.calculateProfit(prices, day + 2, profit + prices[day], False, cache)
        
        cooldown = self.calculateProfit(prices, day + 1, profit, bought, cache)

        maxx = max(buy, sell, cooldown)

        # CHANGE: store relative profit, not absolute
        cache[(day, bought)] = maxx - profit

        return maxx