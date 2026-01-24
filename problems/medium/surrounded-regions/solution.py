"""
Problem: Surrounded Regions
Difficulty: Medium
URL: https://leetcode.com/problems/surrounded-regions/

Time Complexity: O(m * n) where m is number of rows and n is number of columns
Space Complexity: O(m * n) for the visited set in the worst case
"""

"""
Intuition:
DFS from O
if all dirs have X, then valid
if any O in region on border, whole region is invalid
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        borderIdx = {(dr, dc): i for i, (dr, dc) in enumerate(directions)}

        visited, borders, borderCellFound = set(), [False] * 4, False

        def dfs(r, c):
            nonlocal borderCellFound

            if (r, c) in visited:
                return
            visited.add((r, c))

            if r - 1 < 0 or r + 1 == rows or c - 1 < 0 or c + 1 == cols:
                borderCellFound = True
                return

            for dr, dc in directions:
                if not borderCellFound:
                    nr, nc = r + dr, c + dc
                    if board[nr][nc] == "O":
                        dfs(nr, nc)
                    else:
                        borders[borderIdx[(dr, dc)]] = True

        allVisited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in allVisited:
                    dfs(r, c)
                    if not borderCellFound and False not in borders:
                        for row, col in visited:
                            board[row][col] = "X"
                    else:
                        allVisited.update(visited)
                    visited, borders, borderCellFound = set(), [False] * 4, False
