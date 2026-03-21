"""
Problem: Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0, 0]
        sell = 0

        for i in range(n - 1, -1, -1):
            newBuy = max(buy[0], sell - prices[i])
            newSell = max(sell, buy[1] + prices[i])
            buy[0], buy[1], sell = newBuy, buy[0], newSell

        return buy[0]

    # Alternative solution with O(n) space complexity
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = [0] * (n + 2)
        sell = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            buy[i] = max(buy[i + 1], sell[i + 1] - prices[i])
            sell[i] = max(sell[i + 1], buy[i + 2] + prices[i])

        return buy[0]
