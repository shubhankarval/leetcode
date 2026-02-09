"""
Problem: Decode Ways
Difficulty: Medium
URL: https://leetcode.com/problems/decode-ways/

Time Complexity: O(n)
Space Complexity: O(1)
"""

"""
For each digit, decide if to choose digit:
1. individually
2. with the next digit
"""


class Solution:
    # DP Bottom-up
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev2, prev1 = 1, 1  # the results of prev 2 subproblems

        for i in range(1, len(s)):
            curr = 0

            # One-digit decode
            if s[i] != "0":
                curr += prev1

            # Two-digit decode
            two_digit = int(s[i - 1 : i + 1])
            if 10 <= two_digit <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1

    # DP Top-down
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
