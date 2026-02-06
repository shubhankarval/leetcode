"""
Problem: Fibonacci Number
Difficulty: Easy
URL: https://leetcode.com/problems/fibonacci-number/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    # Iterative
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        n1, n2 = 0, 1
        n -= 2
        while n:
            n1, n2 = n2, n1 + n2
            n -= 1
        return n1 + n2

    # Recursive (suboptimal)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    # Recursive DP
    def fib(self, n: int) -> int:
        dp = [0] * (n + 1)

        def rec(n):
            if n == 0 or n == 1:
                return n
            if dp[n]:
                return dp[n]
            dp[n] = rec(n - 1) + rec(n - 2)
            return dp[n]

        return rec(n)
