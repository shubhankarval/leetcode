"""
Problem: Coin Change II
Difficulty: Medium
URL: https://leetcode.com/problems/coin-change-ii/

Time Complexity: O(n^(A / min_coin))
Space Complexity: O(A)
- where A = amount
        n = no. of coins
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        cnt = 0

        def dfs(i, amt):
            nonlocal cnt
            for j in range(i, len(coins)):
                newAmt = amt + coins[j]
                if newAmt == amount:
                    cnt += 1
                elif newAmt < amount:
                    dfs(j, newAmt)

        dfs(0, 0)
        return cnt
