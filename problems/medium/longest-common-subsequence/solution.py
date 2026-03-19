"""
Problem: Longest Common Subsequence
Difficulty: Medium
URL: https://leetcode.com/problems/longest-common-subsequence/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
- where m and n are the lengths of text1 and text2 respectively.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        dp = [[-1] * l2 for _ in range(l1)]

        def dfs(i, j):
            if i == l1 or j == l2:
                return 0
            if dp[i][j] == -1:
                dp[i][j] = 0
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dfs(i + 1, j + 1)
                else:
                    dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        return dfs(0, 0)
