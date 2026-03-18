"""
Problem: Unique Paths
Difficulty: Medium
URL: https://leetcode.com/problems/unique-paths/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[1, 0], [0, 1]]
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = 1

        def dfs(r, c):
            if not dp[r][c]:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        dp[r][c] += dfs(nr, nc)

            return dp[r][c]

        return dfs(0, 0)
