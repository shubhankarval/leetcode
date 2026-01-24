"""
Problem: Islands and Treasure
Difficulty: Medium
URL: https://neetcode.io/problems/islands-and-treasure/

Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid
Space Complexity: O(m * n) for the BFS queue and visited set in the worst case
"""

from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        queue = deque([])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            r, c, dist = queue.popleft()
            if grid[r][c] > 0:
                grid[r][c] = min(grid[r][c], dist)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if grid[nr][nc] != -1:
                        queue.append((nr, nc, dist + 1))
