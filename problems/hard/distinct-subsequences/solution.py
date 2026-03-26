"""
Problem: Distinct Subsequences
Difficulty: Hard
URL: https://leetcode.com/problems/distinct-subsequences/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
- where m and n are the lengths of strings s and t, respectively.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1] * len(t) for _ in range(len(s))]

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] == -1:
                ans = dfs(i + 1, j)
                if s[i] == t[j]:
                    ans += dfs(i + 1, j + 1)
                dp[i][j] = ans
            return dp[i][j]

        return dfs(0, 0)
