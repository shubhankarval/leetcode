"""
Problem: Reverse Bits
Difficulty: Easy
URL: https://leetcode.com/problems/reverse-bits/

Time Complexity: O(1)
Space Complexity: O(1)
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        shift = 31
        while n:
            lastBit = n & 1
            res |= lastBit << shift
            n >>= 1
            shift -= 1
        return res
