"""
Problem: Best Time to Buy and Sell Stock
Difficulty: Easy
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        profit = 0
        while r < len(prices) - 1:
            if prices[r] > prices[r + 1]:
                profit = max(profit, prices[r] - prices[l])
                r = r + 1
                l = r if prices[r] < prices[l] else l
            else:
                r += 1
        return max(profit, prices[r] - prices[l])
