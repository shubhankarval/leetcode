"""
Problem: N-Queens
Difficulty: Hard
URL: https://leetcode.com/problems/n-queens/

Time Complexity: O(n! * n) where n is the size of the board
Space Complexity: O(n²) where n is the size of the board
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res, visited = [], []

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                skip = False
                for row, col in visited:
                    if c == col or abs(r - row) == abs(c - col):
                        skip = True
                        break
                if skip:
                    continue
                board[r][c] = "Q"
                visited.append((r, c))
                dfs(r + 1)
                board[r][c] = "."
                visited.pop()

        dfs(0)
        return res
