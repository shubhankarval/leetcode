"""
Problem: Number of Islands
Difficulty: Medium
URL: https://leetcode.com/problems/number-of-islands/

Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid
Space Complexity: O(m * n) in the worst case for the seen set and recursion stack
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        cntIslands = 0

        def dfs(r, c):
            if (
                not (0 <= r < rows)
                or not (0 <= c < cols)
                or grid[r][c] == "0"
                or (r, c) in seen
            ):
                return
            seen.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    dfs(r, c)
                    cntIslands += 1

        return cntIslands
