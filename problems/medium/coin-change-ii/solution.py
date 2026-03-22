"""
Problem: Coin Change II
Difficulty: Medium
URL: https://leetcode.com/problems/coin-change-ii/

Time Complexity: O(n * a)
Space Complexity: O(a)
- where n = no. of coins
        a = amount
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 1. Sort coins to enable early stopping
        coins.sort()

        # 2. Initialize DP table where dp[i] is the number of ways to make amount i
        # Base case: There is 1 way to make amount 0 (using no coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        # 3. Iterate through each coin
        for coin in coins:
            # EARLY STOP: If the smallest available coin is already
            # larger than the target amount, we can stop entirely.
            if coin > amount:
                break

            # 4. Update the DP table for all amounts from 'coin' up to 'amount'
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[amount]

    # Alternative DP Top-Down Approach (with Space Complexity O(n * a))
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
