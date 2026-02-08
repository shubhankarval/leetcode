"""
Problem: Climbing Stairs
Difficulty: Easy
URL: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    # DP Bottom-up
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1
        for _ in range(2, n + 1):
            n1, n2 = n2, n1 + n2
        return n2

    # DP Top-down
    def climbStairs(self, n: int) -> int:
        dp = [0] * n

        def rec(steps):
            if steps > n:
                return 0
            if steps == n:
                return 1
            if not dp[steps]:
                dp[steps] = rec(steps + 1) + rec(steps + 2)
            return dp[steps]

        return rec(0)
