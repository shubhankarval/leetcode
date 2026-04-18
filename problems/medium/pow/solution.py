"""
Problem: Pow(x, n)
Difficulty: Medium
URL: https://leetcode.com/problems/powx-n/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        prod = 1
        for _ in range(abs(n)):
            prod *= x
        return prod if n >= 0 else 1 / prod
