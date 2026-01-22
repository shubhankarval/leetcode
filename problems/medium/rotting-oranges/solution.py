"""
Problem: Rotting Oranges
Difficulty: Medium
URL: https://leetcode.com/problems/rotting-oranges/

Time Complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid
Space Complexity: O(m * n) for the BFS queue and visited set in the worst case
"""

"""
Intuition: multi-source bfs 

add all rotten fruits to the queue
queue needs to contain r,c,curr min
return min if min else -1
"""

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        totalMin = 0

        rows, cols = len(grid), len(grid[0])
        freshOranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    freshOranges += 1

        if not freshOranges:
            return 0

        while queue:
            currR, currC, currMin = queue.popleft()
            totalMin = currMin
            if grid[currR][currC] == 1:
                freshOranges -= 1

            for nextR, nextC in [
                (currR + 1, currC),
                (currR - 1, currC),
                (currR, currC + 1),
                (currR, currC - 1),
            ]:
                if (
                    0 <= nextR < rows
                    and 0 <= nextC < cols
                    and (nextR, nextC) not in visited
                ):
                    visited.add((nextR, nextC))
                    if grid[nextR][nextC] != 0:
                        queue.append((nextR, nextC, currMin + 1))

        return totalMin if not freshOranges else -1
