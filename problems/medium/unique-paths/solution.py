"""
Problem: Unique Paths
Difficulty: Medium
URL: https://leetcode.com/problems/unique-paths/

Time Complexity: O(2 ^ (m + n))
Space Complexity: O(m + n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[1, 0], [0, 1]]

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            paths = 0

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    paths += dfs(nr, nc)

            return paths

        return dfs(0, 0)
