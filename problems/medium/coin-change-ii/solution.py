"""
Problem: Coin Change II
Difficulty: Medium
URL: https://leetcode.com/problems/coin-change-ii/

Time Complexity: O(n * a)
Space Complexity: O(n * a)
- where n = no. of coins
        a = amount
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * n for _ in range(amount)]

        def dfs(amt, i):
            if i == n:
                return 0
            if amt > amount:
                return 0
            if amt == amount:
                return 1
            if dp[amt][i] == -1:
                dp[amt][i] = dfs(amt + coins[i], i) + dfs(amt, i + 1)
            return dp[amt][i]

        return dfs(0, 0)
