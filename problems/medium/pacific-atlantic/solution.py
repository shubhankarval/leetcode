"""
Problem: Pacific Atlantic Water Flow
Difficulty: Medium
URL: https://leetcode.com/problems/pacific-atlantic-water-flow/

Time Complexity: O(m * n) where m is number of rows and n is number of columns
Space Complexity: O(m * n) for the visited set
"""

"""
Intuition:
dfs from borders of matrix
check which cells >= than prev, add to appr set
return common elements from both sets in list
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        canReachPac, canReachAtl = set(), set()
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c, s):
            if (r, c) in s:
                return
            s.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and heights[r][c] <= heights[nr][nc]
                ):
                    dfs(nr, nc, s)

        for c in range(cols):
            dfs(0, c, canReachPac)
            dfs(rows - 1, c, canReachAtl)

        for r in range(rows):
            dfs(r, 0, canReachPac)
            dfs(r, cols - 1, canReachAtl)

        return list(map(lambda x: list(x), list(canReachPac & canReachAtl)))
