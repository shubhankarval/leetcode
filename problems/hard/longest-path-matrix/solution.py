"""
Problem: Longest Increasing Path in Matrix
Difficulty: Hard
URL: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Time Complexity: O(m * n)
Space Complexity: O(m * n)
- where m and n are the number of rows and columns in the matrix, respectively.
"""

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = [[-1] * cols for _ in range(rows)]
        visited = [[0] * cols for _ in range(rows)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if visited[r][c]:
                return 0
            visited[r][c] = 1

            if memo[r][c] == -1:
                res = 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] > matrix[r][c]
                    ):
                        res = max(res, 1 + dfs(nr, nc))
                memo[r][c] = res

            visited[r][c] = 0
            return memo[r][c]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c)

        return max(max(row) for row in memo)
