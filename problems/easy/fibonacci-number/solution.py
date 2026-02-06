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
        for _ in range(2, n):
            n1, n2 = n2, n1 + n2
        return n1 + n2

    # Recursive (suboptimal)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    # Recursive DP
    def fib(self, n: int) -> int:
        dp = [None] * (n + 2)
        dp[0], dp[1] = 0, 1

        def rec(n):
            if dp[n] == None:
                dp[n] = rec(n - 1) + rec(n - 2)
            return dp[n]

        return rec(n)
