"""
Problem: Fibonacci Number
Difficulty: Easy
URL: https://leetcode.com/problems/fibonacci-number/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        n1, n2 = 0, 1
        fibSum = 0
        while n > 1:
            fibSum = n1 + n2
            n1, n2 = n2, fibSum
            n -= 1
        return fibSum
