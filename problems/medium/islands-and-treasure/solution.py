"""
Problem: Islands and Treasure
Difficulty: Medium
URL: https://neetcode.io/problems/islands-and-treasure/solution

Time Complexity: O((m * n)²) where m is the number of rows and n is the number of columns in the grid
Space Complexity: O(m * n) for the BFS queue and visited set in the worst case
"""

from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = deque([(r, c, 0)])
            visited = set([(r, c)])

            while queue:
                curr_r, curr_c, dist = queue.popleft()

                if grid[curr_r][curr_c] > 0:
                    grid[curr_r][curr_c] = min(grid[curr_r][curr_c], dist)

                for nr, nc in [
                    (curr_r + 1, curr_c),
                    (curr_r - 1, curr_c),
                    (curr_r, curr_c + 1),
                    (curr_r, curr_c - 1),
                ]:
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] != -1:
                            queue.append((nr, nc, dist + 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r, c)
