"""
Problem: Min Cost Climbing Stairs
Difficulty: Easy
URL: https://leetcode.com/problems/min-cost-climbing-stairs/

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        dp = [None] * n

        def rec(step):
            if step >= n:
                return 0
            if dp[step] == None:
                dp[step] = cost[step] + min(rec(step + 1), rec(step + 2))
            return dp[step]

        return rec(-1)
