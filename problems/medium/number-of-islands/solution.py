"""
Problem: Number of Islands
Difficulty: Medium
URL: https://leetcode.com/problems/number-of-islands/

Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid
Space Complexity: O(m * n) in the worst case for recursion stack
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cntIslands = 0

        def dfs(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols) or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for row, col in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(row, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    cntIslands += 1

        return cntIslands
