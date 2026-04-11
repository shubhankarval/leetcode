"""
Problem: Number of 1 Bits
Difficulty: Easy
URL: https://leetcode.com/problems/number-of-1-bits/

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        mask = 1
        for _ in range(32):
            if n & mask > 0:
                cnt += 1
            mask <<= 1
        return cnt
