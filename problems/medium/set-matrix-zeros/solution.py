"""
Problem: Set Matrix Zeroes
Difficulty: Medium
URL: https://leetcode.com/problems/set-matrix-zeroes/

Time Complexity: O(m * n)
Space Complexity: O(m + n)
- where m = the number of rows
        n = the number of columns
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeroRows, zeroCols = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0
