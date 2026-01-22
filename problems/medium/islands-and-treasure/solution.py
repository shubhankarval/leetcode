"""
Problem: Islands and Treasure
Difficulty: Medium
URL: https://neetcode.io/problems/islands-and-treasure/solution

Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid
Space Complexity: O(m * n) for the BFS queue and visited set in the worst case
"""

from typing import List
from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))

        while queue:
            currR, currC, currDist = queue.popleft()
            if grid[currR][currC] > 0:
                grid[currR][currC] = min(grid[currR][currC], currDist)

            for newR, newC in [
                (currR + 1, currC),
                (currR - 1, currC),
                (currR, currC + 1),
                (currR, currC - 1),
            ]:
                if (
                    0 <= newR < rows
                    and 0 <= newC < cols
                    and (newR, newC) not in visited
                ):
                    visited.add((newR, newC))
                    if grid[newR][newC] != -1:
                        queue.append((newR, newC, currDist + 1))
