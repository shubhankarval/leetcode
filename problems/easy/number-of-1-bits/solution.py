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
        while n:
            n &= n - 1
            cnt += 1
        return cnt

    # Alternative solution
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n:
            if n & 1:
                cnt += 1
            n >>= 1
        return cnt
