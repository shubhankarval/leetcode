"""
Problem: Surrounded Regions
Difficulty: Medium
URL: https://leetcode.com/problems/surrounded-regions/

Time Complexity: O(m * n) where m is number of rows and n is number of columns
Space Complexity: O(m * n) for the visited set in the worst case
"""

"""
Intuition:
DFS from O on borders and mark all visited O cells
make all other cells as X
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    dfs(nr, nc)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = "X"
