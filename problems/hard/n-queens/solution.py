"""
Problem: N-Queens
Difficulty: Hard
URL: https://leetcode.com/problems/n-queens/

Time Complexity: O(n!) where n is the size of the board
Space Complexity: O(n²) where n is the size of the board
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        cols, posD, negD = set(), set(), set()

        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or row + col in posD or row - col in negD:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                posD.add(row + col)
                negD.add(row - col)

                dfs(row + 1)

                board[row][col] = "."
                cols.remove(col)
                posD.remove(row + col)
                negD.remove(row - col)

        dfs(0)
        return res
