"""
Problem: Pacific Atlantic Water Flow
Difficulty: Medium
URL: https://leetcode.com/problems/pacific-atlantic-water-flow/

Time Complexity: O((m * n)²) where m is number of rows and n is number of columns
Space Complexity: O(m * n) for the visited set
"""

"""
Intuition:
Dfs from each cell
Check if it can reach any cell adj to each ocean:
1. top & left for pacific
2. bottom and right for atlantic
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = atlantic = False
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(r, c):
            nonlocal pacific, atlantic
            visited.add((r, c))
            if r - 1 == -1 or c - 1 == -1:
                pacific = True
            if r + 1 == rows or c + 1 == cols:
                atlantic = True
            if pacific and atlantic:
                return
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    (not pacific or not atlantic)
                    and 0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[r][c] >= heights[nr][nc]
                ):
                    dfs(nr, nc)

        res = []
        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
                if pacific and atlantic:
                    res.append([r, c])
                elif not pacific and not atlantic:
                    heights[r][c] = 10**5 + 1
                pacific = atlantic = False
                visited = set()

        return res
