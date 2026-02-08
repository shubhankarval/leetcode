"""
Problem: Decode Ways
Difficulty: Medium
URL: https://leetcode.com/problems/decode-ways/

Time Complexity: O(2ⁿ)
Space Complexity: O(n)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        def rec(idx, prev):
            if idx >= len(s):
                return 1
            curr = prev + s[idx]
            if not 1 <= int(curr) <= 26:
                return 0
            return rec(idx + 1, "") + rec(idx + 1, curr)

        return rec(0, "") // 2
