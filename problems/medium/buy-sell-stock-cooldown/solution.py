"""
Problem: Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Time Complexity: O(2ⁿ)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        def dfs(i, buy, profit):
            nonlocal res
            if i >= len(prices):
                return
            for j in range(i, len(prices)):
                if buy:
                    dfs(j + 1, False, profit - prices[j])
                else:
                    res = max(res, profit + prices[j])
                    dfs(j + 2, True, profit + prices[j])

        dfs(0, True, 0)
        return res
