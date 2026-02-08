"""
Problem: Climbing Stairs
Difficulty: Easy
URL: https://leetcode.com/problems/climbing-stairs/

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2 = 1, 1
        for _ in range(2, n + 1):
            n1, n2 = n2, n1 + n2
        return n2
