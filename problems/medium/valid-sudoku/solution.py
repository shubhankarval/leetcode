"""
Problem: Valid Sudoku
Difficulty: Medium
URL: https://leetcode.com/problems/valid-sudoku/
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.containsDuplicate(row):
                return False

        for col in range(0, 9):
            lst = []
            for row in range(0, 9):
                lst.append(board[row][col])
            if self.containsDuplicate(lst):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                lst = []
                for sub_row in range(row, row + 3):
                    lst.extend(board[sub_row][col : col + 3])
                if self.containsDuplicate(lst):
                    return False

        return True

    def containsDuplicate(self, lst: List[str]) -> bool:
        only_nums = [x for x in lst if x != "."]
        return len(only_nums) != len(set(only_nums))
