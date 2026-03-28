"""
Problem: Edit Distance
Difficulty: Medium
URL: https://leetcode.com/problems/edit-distance/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
- where m = len(word1)
        n = len(word2)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[-1] * l2 for _ in range(l1)]

        def dfs(i, j):
            if j == l2:
                return l1 - i
            if i == l1:
                return l2 - j
            if dp[i][j] == -1:
                if word1[i] == word2[j]:
                    dp[i][j] = dfs(i + 1, j + 1)
                else:
                    dp[i][j] = 1 + min(dfs(i + 1, j + 1), dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        return dfs(0, 0)
