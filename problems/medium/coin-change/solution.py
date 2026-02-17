"""
Problem: Coin Change
Difficulty: Medium
URL: https://leetcode.com/problems/coin-change/

Time Complexity: O(n * m) where n is the target amount and m is the number of coins
Space Complexity: O(n) where n is the target amount
"""

"""
return min no. of coins, such that sum(coins) == target amount
unlimited number of each coin
if sum(coins) != target amt, return -1

Soln:
dfs with loop
two ways:
1. start with target amt, stop when amt is <= 0
2. start with 0, stop when amt >= target

soln 1 is preferrable since we can return num of coins recursively
whereas for soln 2 we need to have a var for tracking min coins

dfs params: amount (starting with target amount)
max no. of coins possible is target amt (using only 1s)
"""

from typing import List


class Solution:
    # DP Bottom-Up
    def coinChange(self, avlblCoins: List[int], targetAmt: int) -> int:
        dp = [targetAmt + 1] * (targetAmt + 1)
        dp[0] = 0

        for amt in range(1, targetAmt + 1):
            for coin in avlblCoins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])

        return -1 if dp[targetAmt] > targetAmt else dp[targetAmt]

    # DP Top-Down
    def coinChange(self, avlblCoins: List[int], targetAmt: int) -> int:
        maxCoins = targetAmt + 1  # 1 plus max no. of coins possible
        dp = [0] * maxCoins

        def dfs(amt):
            if not dp[amt]:
                if amt == 0:
                    return 0
                if amt < 0:
                    return maxCoins

                dp[amt] = maxCoins
                for coin in avlblCoins:
                    if amt >= coin:
                        dp[amt] = min(1 + dfs(amt - coin), dp[amt])

            return dp[amt]

        ans = dfs(targetAmt)
        return -1 if ans > targetAmt else ans
