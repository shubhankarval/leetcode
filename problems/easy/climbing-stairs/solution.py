"""
Problem: Climbing Stairs
Difficulty: Easy
URL: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 2)

        def rec(steps):
            if steps > n:
                return 0
            if steps == n:
                return 1
            if not dp[steps + 1]:
                dp[steps + 1] = rec(steps + 1)
            if not dp[steps + 2]:
                dp[steps + 2] = rec(steps + 2)
            return dp[steps + 1] + dp[steps + 2]

        return rec(0)
