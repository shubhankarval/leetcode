"""
Problem: Number of 1 Bits
Difficulty: Easy
URL: https://leetcode.com/problems/number-of-1-bits/

Time Complexity: O(k)
Space Complexity: O(k)
- where k = number of bits in the binary representation of n
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
