"""
Problem: Decode Ways
Difficulty: Medium
URL: https://leetcode.com/problems/decode-ways/

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}

        def rec(idx, prev):
            if idx >= len(s):
                return 1
            if (idx, prev) not in dp:
                curr = prev + s[idx]
                if not 1 <= int(curr) <= 26:
                    return 0
                dp[(idx, prev)] = rec(idx + 1, "") + rec(idx + 1, curr)
            return dp[(idx, prev)]

        return rec(0, "") // 2
