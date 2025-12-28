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

        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                skip = False
                for prevRow, prevCol in visited:
                    if col == prevCol or row - prevRow == abs(col - prevCol):
                        skip = True
                        break
                if skip:
                    continue
                board[row][col] = "Q"
                visited.append((row, col))
                dfs(row + 1)
                board[row][col] = "."
                visited.pop()

        dfs(0)
        return res
