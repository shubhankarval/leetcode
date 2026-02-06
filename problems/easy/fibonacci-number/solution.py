"""
Problem: Fibonacci Number
Difficulty: Easy
URL: https://leetcode.com/problems/fibonacci-number/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        n1, n2 = 0, 1
        n -= 2
        while n:
            n1, n2 = n2, n1 + n2
            n -= 1
        return n1 + n2
