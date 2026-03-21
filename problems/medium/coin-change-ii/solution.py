"""
Problem: Coin Change II
Difficulty: Medium
URL: https://leetcode.com/problems/coin-change-ii/

Time Complexity: O(n² * a)
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
            if amt > amount:
                return 0
            if amt == amount:
                return 1
            if dp[amt][i] == -1:
                cnt = 0
                for j in range(i, n):
                    cnt += dfs(amt + coins[j], j)
                dp[amt][i] = cnt
            return dp[amt][i]

        return dfs(0, 0)
