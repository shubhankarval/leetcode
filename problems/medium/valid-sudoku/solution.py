"""
Problem: Valid Sudoku
Difficulty: Medium
URL: https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for val in row:
                if self.containsDuplicate(val, s):
                    return False

        for col in range(9):
            s = set()
            for row in range(9):
                if self.containsDuplicate(board[row][col], s):
                    return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                s = set()
                for sub_row in range(row, row + 3):
                    for sub_col in range(col, col + 3):
                        if self.containsDuplicate(board[sub_row][sub_col], s):
                            return False

        return True

    def containsDuplicate(self, val: str, s: set) -> bool:
        if val in s:
            return True
        if val != ".":
            s.add(val)
        return False
